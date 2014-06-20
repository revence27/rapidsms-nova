# encoding: utf-8
# vim: expandtab ts=2

import copy
from datetime import datetime, date, time
from decimal import Decimal
from ..messages.parser import *
from ....settings import __DEFAULTS, THE_DATABASE as postgres
import psycopg2
import re
from sys import stderr

class ThouQuery:
  def __init__(self, djconds, tn, **kwargs):
    self.djconds = djconds
    self.tablenm = kwargs.get('table', tn)
    self.kwargs  = kwargs
    self.cursor  = None
    self.names   = kwargs.get('cols', [])

  def set_names(self, dat):
    self.names  = dat.keys()
    self.cols   = dat

  def active_columns(self, qid):
    return self.names or ThouReport.active_columns(qid)

  def assemble_conditions(self, conds):
    return ThouReport.assemble_conditions(conds)

  def filter(self, **kwargs):
    nova  = copy.copy(self)
    for k in kwargs:
      nova.djconds[k] = kwargs[k]
    return nova

  def order_by(self, cue):
    raise Exception, ('TODO %s' % (cue,))
    return self

  def count(self):
    if not self.cursor:
      self.execute()
    return max(0, self.cursor.rowcount)

  def execute(self):
    if not self.cursor:
      self.names, self.cursor = self.__execute()
      self.cols               = self.__set_names()
    return self

  def __getitem__(self, them):
    if not self.cursor:
      self.execute()
      return self[them]
    dem = []
    try:
      for ent in self.cursor.fetchmany(them.stop - them.start):
        ans = {}
        for nom in self.names:
          got       = ent[self.cols[nom]]
          if got:
            ans[nom] = got
        dem.append(ans)
    except IndexError:
      pass
    return dem

  def old__getitem__(self, them):
    if type(them) != slice:
      raise ValueError, ('Should be a slice [column-name:row], not a %s (%s)' % (type(them), str(them)))
    try:
      return them.stop[self.names[them.start]]
    except ValueError:
      raise NameError, ('No column called "%s" (has: %s).' % (colnm, ', '.join(cols)))

  def __set_names(self):
    self.cols   = {}
    notI        = 0
    for x in self.names:
      self.cols[x]  = notI
      notI          = notI + 1
    return self.cols

  # TODO: Work with views to ensure closing of cursors.
  def __execute(self):
    qry   = self.query
    # TODO: remove this.
    stderr.write('%s\r\n' % (qry,))
    curz        = postgres.cursor()
    curz.execute(qry)
    cols  = [x.name for x in curz.description]
    return (cols, curz)

  def close(self):
    if not self.cursor: return
    return self.cursor.close()

  def __enter__(self):
    pass  # For now.

  def __exit__(self, *args):
    self.close()

  @property
  def query(self):
    qry = u'SELECT %s FROM %s %s' % (', '.join(self.kwargs.get('cols', self.active_columns(self.kwargs.get('qid')) or ['*'])), self.tablenm, self.assemble_conditions(self.djconds))
    return qry

  def __unicode__(self):
    return self.query

# TODO:
# Load the report(s).
# Find a report.
class ThouReport:
  'The base class for all "RapidSMS 1000 Days" reports.'
  created   = False
  columned  = False

  def __init__(self, msg):
    'Initialised with the Message object to which it is coupled.'
    self.msg  = msg

  def __insertables(self, fds):
    '''Returns a hash of all the columns that will be affected by an insertion of this report into the database. The column name is the key, with its value.'''
    cvs   = {}
    ents  = self.msg.entries
    for fx in ents:
      curfd = ents[fx]
      if curfd.several_fields:
        for vl in curfd.working_value:
          cvs[('%s_%s' % (fx, vl)).lower()] = vl
      else:
        try:
          cvs[fx] = curfd.working_value[0]
        except IndexError:
          raise Exception, ('No value supplied for column \'%s\' (%s)' % (fx, str(curfd)))
    return cvs

  # TODO: Consider the message field classes' declared default.
  def save(self):
    return self.__class__.sparse_matrix(self)

  def old_save(self):
    '''This method saves the report object into the table for that report class, returning the index as an integer.
It is not idempotent at this level; further constraints should be added by inheriting classes.'''
    tbl, cols = self.msg.__class__.create_in_db(self.__class__)
    cvs       = self.__insertables(cols)
    curz      = THE_DATABASE.cursor()
    cpt       = []
    vpt       = []
    for coln, _, escer, _ in cols:
      if coln in cvs:
        cpt.append(coln)
        vpt.append(escer.dbvalue(cvs[coln], curz))
    qry = 'INSERT INTO %s (%s) VALUES (%s) RETURNING indexcol;' % (tbl, ', '.join(cpt), ', '.join(vpt)) 
    curz.execute(qry)
    ans = curz.fetchone()[0]
    curz.close()
    return ans

  @classmethod
  def alter_condition(self, conds, ok):
    if not ok in conds:
      return ok, None
    idem    = lambda x: x
    newks   = {
      'type'        : ('report_type = %s', lambda x: x.name),
      'nation__id'  : ('nation_pk = %s', idem)
}
    nk, nv  = newks[ok]
    return (nk, nv(conds[ok]) if type(nv) == type(idem) else nv)

  # TODO: map old filters to new DB structure.
  @classmethod
  def assemble_conditions(self, conds):
    # TODO: review condition-handling.
    curz  = postgres.cursor()
    ans   = []
    for cond in conds:
      nk, nv  = self.alter_condition(conds, cond)
      ans.append(curz.mogrify(nk, (nv,)))
    curz.close()
    return (' WHERE ' if conds else '') + ' AND '.join(ans)

  seen_actives  = {}
  @classmethod
  def active_columns(self, qid = None):
    if not qid: return qid
    if not qid in self.seen_actives: return None
    return seen_actives[qid]

  @classmethod
  def record_activity(self, qid, qnom):
    if not qid in self.seen_actives:
      self.seen_actives[qid] = set()
      return self.record_activity(qid, qnom)
    us  = self.seen_actives[qid]
    us.add(qnom)
    return us

  @classmethod
  def old_query(self, djconds, tn = None, **kwargs):
    if not tn: return self.query(djconds, kwargs.get('table', __DEFAULTS['REPORTS']))
    tbl = self.ensure_table(tn)
    qry = 'SELECT %s FROM %s %s' % (', '.join(kwargs.get('cols', self.active_columns(kwargs.get('qid')) or ['*'])), tbl, self.assemble_conditions(djconds))
    curz  = postgres.cursor()
    # TODO: remove this.
    stderr.write('%s\r\n' % (qry,))
    curz.execute(qry)
    cols  = [x.name for x in curz.description]
    ans   = curz.fetchall()
    curz.close()
    postgres.commit()
    return (cols, ans)

  @classmethod
  def query(self, tn, djconds, **kwargs):
    if not tn: return self.query(kwargs.get('table', __DEFAULTS['REPORTS']), djconds, **kwargs)
    tbl = self.ensure_table(tn)
    return ThouQuery(djconds, tn, **kwargs)

  @classmethod
  def find_matching_type(self, val, ctyp, cn = None):
    try:
      return {
        str:       ctyp,
        unicode:   ctyp,
        int:       'INTEGER /*NOT NULL*/',
        long:      'INTEGER /*NOT NULL*/',
        float:     'FLOAT /*NOT NULL*/',
        bool:      'BOOLEAN /*NOT NULL*/',
        Decimal:   'FLOAT /*NOT NULL*/',
        datetime:  'TIMESTAMP',
        date:      'TIMESTAMP WITHOUT TIME ZONE',
        time:      'TIMESTAMP'
      }[type(val)]
    except KeyError:
      raise Exception, ('Supply type for column %s (has a %s, %s)?' % (cn, str(type(val)), str(val)))

  @classmethod
  def decide_type(self, vl, cn = None):
    ctyp  = 'TEXT DEFAULT NULL'
    dval  = vl
    if type(vl) == type((None, 'INTEGER DEFAULT NULL')):
      ctyp  = vl[1]
      dval  = vl[0]
    elif type(vl) == type({'type':'INTEGER', 'null':False, 'default':'', 'value':None}):
      dval  = vl.get('value')
      ddef  = vl.get('default')
      dstr  = '%s %s%s' % (vl.get('type') or self.find_matching_type(dval, ctyp, cn), '' if vl.get('null') else 'NOT NULL', (' DEFAULT ' + ddef if ddef else ''))
      return self.decide_type((dval, dstr), cn)
    else:
      ctyp  = self.find_matching_type(vl, ctyp, cn)
      return self.decide_type((dval, ctyp), cn)
    return ctyp, dval

  seen_columns  = set()
  @classmethod
  def store(self, dat, tn = None):
    if not tn: return self.store(dat, __DEFAULTS['REPORTS'])
    if type(dat) == type([]):
      return [self.store(cv, tn) for cv in dat]
    if not dat: return None
    cols  = dat.keys()
    vals  = []
    curz  = postgres.cursor()
    tbl   = self.ensure_table(tn)
    ans   = dat.get('indexcol')
    for col in cols:
      dval  = dat[col]
      if not col in self.seen_columns:
        curz.execute('SELECT TRUE FROM information_schema.columns WHERE table_name = %s AND column_name = %s', (tbl, col))
        if not curz.fetchone():
          ctyp, dval  = self.decide_type(dval, col)
          curz.execute('ALTER TABLE %s ADD COLUMN %s %s;' % (tbl, col, ctyp))
          self.seen_columns.add(col)
      elval = curz.mogrify('%s', (dval, ))
      if ans:
        dat[col]  = elval
      else:
        vals.append(elval)
    if vals:
      curz.execute('INSERT INTO %s (%s) VALUES (%s) RETURNING indexcol;' % (tbl, ', '.join(cols), ', '.join(vals)))
      ans = curz.fetchone()[0]
    else:
      curz.execute('UPDATE %s SET %s WHERE indexcol = %d;' % (tbl, ', '.join(['%s = %s' % (k, dat[k]) for k in dat]), ans))
    postgres.commit()
    curz.close()
    return ans

  seen_tables = set()
  @classmethod
  def ensure_table(self, tbl = None):
    try:
      tbl   = (tbl or __DEFAULTS['REPORTS'])
      if tbl in self.seen_tables: return tbl
      curz  = postgres.cursor()
      curz.execute('SELECT TRUE FROM information_schema.tables WHERE table_name = %s', (tbl,))
      if not curz.fetchone():
        curz.execute('CREATE TABLE %s (indexcol SERIAL NOT NULL, created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW());' % (tbl,))
        curz.close()
      self.seen_tables.add(tbl)
      return tbl
    except Exception, e:
      raise Exception, ('Table creation: ' + str(e))

  @classmethod
  def sparse_matrix_store(self, hsh):
    tbl = self.ensure_table()
    return self.store(hsh, tbl)

  @classmethod
  def sparse_matrix(self, tn, cvs = None, prep = None):
    if not cvs:
      if issubclass(tn.__class__, self):
        tn, cols = self.msg.__class__.creation_sql(self.__class__)
        return self.sparse_matrix(tn, self.__insertables(cols), prep)
      raise ValueError, 'sparse_matrix wants a (string, hash), a (string, [hash]), or a (ThouReport). There is always an optional string after (super-table name).'
    if type(cvs) == type([]):
      return [self.sparse_matrix(tn, cv, prep) for cv in cvs]
    if type(cvs) == type({}):
      fxnms = {}
      for cvk in cvs:
        fxnms['%s_%s' % (tn, cvk)]  = cvs[cvk]
      return self.sparse_matrix_store(fxnms)
    raise Exception, ('What sparse matrix is %s?' % (str(cvs),))

  @classmethod
  def load(self, msgtxt):
    with ThouMessage.parse(msgtxt) as msg:
      return self(msg)

class BasicConverter:
  def __init__(self):
    self.types  = ReportType.objects.all()
    self.thash  = self.__type_hash()

  def __type_hash(self):
    ans = {}
    for t in self.types:
      ans[t.pk] = {
        'ANC':'ANC',
        'Birth':'BIR',
        'Case Management Response':'CMR',
        'Child Health':'CHI',
        'Community Based Nutrition':'CBN',
        'Community Case Management':'CCM',
        'Death':'DTH',
        'Departure':'DEP',
        'Newborn Care':'NBC',
        'PNC':'PNC',
        'Pregnancy':'PRE',
        'Red Alert':'RED',
        'Red Alert Result':'RAR',
        'Refusal':'REF',
        'Risk':'RISK',
        'Risk Result':'RES'
      }[t.name]
    return ans

  def __getitem__(self, k):
    return self.thash[k]

class OldStyleReport:
  def __init__(self, rep, cur, cvr):
    self.autos  = rep
    self.conver = cvr
    self.cursor = cur
    self.ftypes = self.__type_hash()

  def __type_hash(self):
    ans = {}
    for fdt in FieldType.objects.all():
      it = {'category_pk': fdt.category.pk, 'key': fdt.key}
      ans[fdt.pk] = it
    return ans

  def __getitem__(self, k):
    return self.ftypes[k]

  @property
  def db_prepend(self):
    return self.conver[self.autos.type.pk].lower()

  @property
  def report_type(self):
    return self.conver[self.autos.type.pk]

  @property
  def message(self):
    return str(self)

  @property
  def reporter(self):
    return self.autos.reporter

  @property
  def patient(self):
    return self.autos.patient

  @property
  def hc(self):
    return self.autos.location

  @property
  def district(self):
    return self.autos.location.district

  @property
  def province(self):
    return self.autos.location.province

  @property
  def nation(self):
    return self.autos.location.nation

  # TODO:
  # 1.  The reports. With types. With fields.
  # 2.  Facilities.
  # 3.  Health workers
  # 4.  Locations
  # 5.  Reports.
  # 6.  Messages
  # 7.  Patients
  def __gather_fields(self, hsh):
    fds = Field.objects.filter(report = self.autos)
    prp = self.db_prepend
    for fd in fds:
      ftype     = fd.type
      cle       = ftype.key
      typedata  = self[ftype.pk]
      typedata[self.__val_name(fd)] = fd.value if ftype.has_value else (fd.value and True or False)
      for td in typedata:
        nom       = '%s_%s_%s' % (prp, cle, td)
        hsh[nom]  = typedata[td]
    return hsh

  def __val_name(self, fd):
    mid = 'bool'
    if fd.type.has_value:
      mid = ThouReport.find_matching_type(fd.value, mid, None)
    return re.split(r'\s+', mid, 2)[0].lower()

  def __as_hash(self):
    ans = {}
    ans['report_type']        = self.report_type
    ans['former_pk']          = self.autos.pk
    ans['reconstructed_msg']  = self.message
    ans['reporter_pk']        = self.reporter.pk
    ans['reporter_phone']     = self.reporter.telephone_moh
    ans['patient_id']         = self.patient.national_id
    ans['patient_pk']         = self.patient.pk
    ans['report_date']        = self.autos.created
    ans['health_center_pk']   = self.hc.pk
    ans['province_pk']        = self.province.pk
    ans['district_pk']        = self.district.pk
    ans['nation_pk']          = self.nation.pk
    return self.__gather_fields(ans)

  def convert(self):
    dat = self.__as_hash()
    thr = ThouReport.store(dat, 'testing_report_transfers')
    return thr

  # TODO: either fetch the message from the DB, or re-construct it. How silly of RapidSMS to not relate the report and its message!
  def __str__(self):
    return '%s TESTER' % (self.conver[self.autos.type.pk],)