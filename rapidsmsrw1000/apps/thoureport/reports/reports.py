# encoding: utf-8
# vim: expandtab ts=2

from ..messages.parser import *
from ....settings import __DEFAULTS, THE_DATABASE as postgres
import psycopg2
import re

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
  def assemble_conditions(self, conds):
    # TODO: skip conditions, for now.
    conds = {}
    curz  = postgres.cursor()
    ans   = []
    for cond in conds:
      it  = conds[cond]
      ans.append(curz.mogrify(cond, it))
    curz.close()
    return (' WHERE ' if conds else '') + ' AND '.join(ans)

  @classmethod
  def query(self, djconds, tn = None):
    if not tn: return self.query(djconds, __DEFAULTS['REPORTS'])
    tbl = self.ensure_table(tn)
    qry = 'SELECT * FROM %s %s' % (tbl, self.assemble_conditions(djconds))
    curz  = postgres.cursor()
    curz.execute(qry)
    cols  = [x.name for x in curz.description]
    ans   = curz.fetchall()
    curz.close()
    postgres.commit()
    return (cols, ans)

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
          ctyp  = 'TEXT DEFAULT NULL'
          try:
            if type(dval) == type((None, '')):
              ctyp  = dval[1]
              dval  = dval[0]
            else:
              # TODO: make ctyp reflect the postgres DB column creation data, including type, if none is supplied.
              pass
          except Exception:
            pass
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

class ThouTable:
  def __init__(self, cols, rows = None):
    self.names  = cols
    self.__set_names()
    self.query  = rows

  def __set_names(self):
    self.cols   = {}
    notI        = 0
    for x in self.names:
      self.cols[x]  = notI
      notI          = notI + 1

  # TODO: filter kind-a like QuerySet.
  def filter(self, **kwargs):
    return self

  def order_by(self, cue):
    return self

  def count(self):
    return len(self.query)

  def rows(self, *args):
    return self.query

  def __getitem__(self, them):
    dem = []
    try:
      for ent in self.query[them.start:them.stop]:
        ans = {}
        for nom in self.names:
          ans[nom] = ent[self.cols[nom]]
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
