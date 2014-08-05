#!  /usr/bin/env python

import cherrypy
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import os, sys, thread
from rapidsmsrw1000.apps.orm import orm
import re
import settings
import subprocess

MONTHS  = 12
BMI_MIN = 19
BMI_MAX = 25
orm.ORM.connect(dbname  = 'thousanddays', user = 'thousanddays', host = 'localhost', password = 'thousanddays')

class ThousandDays:
  def __init__(self, pth, bst, stp, **kw):
    self.path   = pth
    self.jinja  = Environment(loader = FileSystemLoader(pth))
    self.base   = bst
    self.static = stp
    self.jinja.filters.update(kw.get('filters', {}))

  @cherrypy.expose
  def index(self, *args, **kw):
    return self.dynamised('index', *args, **kw)

  def app_data(self):
    try:
      return settings.APP_DATA
    except:
      pass
    return {}

  @cherrypy.expose
  def dynamised(self, chart, mapping = {}, *args, **kw):
    info  = {}
    info.update({
      'base_template' : self.base,
      'ref'           : chart,
      'locations'     : ['TODO'],
      'args'          : kw,
      'nav'           : ThousandNavigation(*args, **kw),
      'static_path'   : self.static
    })
    info.update(self.app_data())
    info.update(kw)
    mapping.pop('self', None)
    info.update({'display': mapping})
    return self.jinja.get_template('%s.html' % (chart, )).render(*args, **info)

class ThousandNavigation:
  def __init__(self, *args, **kw):
    self.args   = args
    self.kw     = kw
    td          = datetime.today()
    self.fin    = datetime(year = td.year, month = td.month, day = td.day)
    self.gap    = timedelta(days = 1000)

  def conditions(self, tn = 'created_at'):
    ans = {
      (tn + ' >= %s')  : self.start,
      (tn + ' <= %s')  : self.finish
    }
    return ans

  @property
  def start(self):
    gat = self.kw.get('start', '')
    if not gat:
      return self.fin - self.gap
    return self.make_time(gat)

  @property
  def finish_date(self):
    return self.text_date(self.finish)

  @property
  def start_date(self):
    return self.text_date(self.start)

  def text_date(self, dt):
    return dt.strftime('%d/%m/%Y')

  @property
  def finish(self):
    gat = self.kw.get('finish', '')
    if not gat:
      return self.fin
    return self.make_time(gat)

  def make_time(self, txt):
    '''dd/mm/yyyy'''
    pcs = [int(x) for x in re.split(r'\D', txt)]
    return datetime(year = pcs[2], month = pcs[1], day = pcs[0])

class ThousandCharts(ThousandDays):
  @cherrypy.expose
  def charts(self, *args, **kw):
    return ':-\\'

  @cherrypy.expose
  def delivery(self, *args, **kw):
    return self.dynamised('delivery', *args, **kw)

  @cherrypy.expose
  def vaccination(self, *args, **kw):
    return self.dynamised('vaccination', *args, **kw)

  @cherrypy.expose
  def nutrition(self, *args, **kw):
    nut = orm.ORM.query('cbn_table',
      cols      = ['COUNT(*) AS allnuts'],
      annotate  = {
        'notbreast':('COUNT(*)', 'nb_bool IS NOT NULL'),
        'breast':('COUNT(*)', 'ebf_bool IS NOT NULL OR cbf_bool IS NOT NULL'),
        'unknown':('COUNT(*)', 'cbf_bool IS NULL AND ebf_bool IS NULL AND nb_bool IS NULL')
      }
    )
    weighed = orm.ORM.query('pre_table', {
      'mother_height_float > 100.0 AND mother_weight_float > 15.0':''
      },
      cols      = ['COUNT(*) AS mums'],
      annotate  = {
        'short':('COUNT(*)', 'mother_height_float < 150.0'),
      }
    )
    thins   = weighed.specialise({'(mother_weight_float / ((mother_height_float * mother_height_float) / 10000.0)) < %s': BMI_MIN})
    fats    = weighed.specialise({'(mother_weight_float / ((mother_height_float * mother_height_float) / 10000.0)) > %s': BMI_MAX})
    bir = orm.ORM.query('bir_table',
      cols      = ['COUNT(*) AS allbirs'],
      annotate  = {
        'hour1':('COUNT(*)', 'bf1_bool IS NOT NULL')
      }
    )
    return self.dynamised('nutrition', mapping = locals(), *args, **kw)

  @cherrypy.expose
  def pregnancy(self, *args, **kw):
    navb    = ThousandNavigation(*args, **kw)
    cnds    = navb.conditions('report_date')
    cits    = cnds.items()
    nat     = orm.ORM.query('pre_table', cnds,
      cols      = ['COUNT(*) AS allpregs'],
      annotate  = {
        'coughing':('COUNT(*)', dict([('ch_bool IS NOT NULL', '')] + cits)),
        'diarrhoea':('COUNT(*)',  dict([('di_bool IS NOT NULL', '')] + cits)),
        'fever':('COUNT(*)',  dict([('fe_bool IS NOT NULL', '')] + cits)),
        'oedema':('COUNT(*)',  dict([('oe_bool IS NOT NULL', '')] + cits)),
        'pneumo':('COUNT(*)',  dict([('pc_bool IS NOT NULL', '')] + cits)),
        'disab':('COUNT(*)',  dict([('db_bool IS NOT NULL', '')] + cits)),
        'cordi':('COUNT(*)',  dict([('ci_bool IS NOT NULL', '')] + cits)),
        'necks':('COUNT(*)',  dict([('ns_bool IS NOT NULL', '')] + cits)),
        'malaria':('COUNT(*)',  dict([('ma_bool IS NOT NULL', '')] + cits)),
        'vomiting':('COUNT(*)',  dict([('vo_bool IS NOT NULL', '')] + cits)),
        'stillb':('COUNT(*)',  dict([('sb_bool IS NOT NULL', '')] + cits)),
        'jaun':('COUNT(*)',  dict([('ja_bool IS NOT NULL', '')] + cits)),
        'hypoth':('COUNT(*)',  dict([('hy_bool IS NOT NULL', '')] + cits)),
        'ibibari':('COUNT(*)',  dict([('ib_bool IS NOT NULL', '')] + cits))
      },
      migrations  = [
        ('db_bool', False),
        ('fe_bool', False),
        ('ma_bool', False),
        ('to_bool', False),
        ('ch_bool', False),
        ('vo_bool', False),
        ('ja_bool', False),
        ('ns_bool', False),
        ('pc_bool', False),
        ('ci_bool', False),
        ('oe_bool', False),
        ('di_bool', False),
        ('sb_bool', False),
        ('hy_bool', False),
        ('hw_bool', False),
        ('gs_bool', False),
        ('mu_bool', False),
        ('rm_bool', False),
        ('ol_bool', False),
        ('yg_bool', False),
        ('kx_bool', False),
        ('yj_bool', False),
        ('lz_bool', False),
        ('ib_bool', False)
      ]
    )
    toi     = nat.specialise({'to_bool IS NOT NULL':''})
    hnd     = nat.specialise({'hw_bool IS NOT NULL':''})
    weighed = nat.specialise({'mother_height_float > 100.0 AND mother_weight_float > 15.0':''})
    thinq   = weighed.specialise({'(mother_weight_float / ((mother_height_float * mother_height_float) / 10000.0)) < %s': BMI_MIN})
    fatq    = weighed.specialise({'(mother_weight_float / ((mother_height_float * mother_height_float) / 10000.0)) > %s': BMI_MAX})
    riskhsh = {'(gs_bool IS NOT NULL OR mu_bool IS NOT NULL OR rm_bool IS NOT NULL OR ol_bool IS NOT NULL OR yg_bool IS NOT NULL OR kx_bool IS NOT NULL OR yj_bool IS NOT NULL OR lz_bool IS NOT NULL)':''}
    riskys  = nat.specialise(riskhsh)
    info    = nat[0]
    rez     = orm.ORM.query('res_table',
      cnds,
      cols        = ['COUNT(*) AS allreps'],
    )
    recovs  = rez.specialise({'mw_bool IS NOT NULL':''})
    aarecov = recovs.specialise({'aa_bool IS NOT NULL':''})
    prrecov = recovs.specialise({'pr_bool IS NOT NULL':''})
    total   = nat[0]['allpregs']
    totalf  = float(total)
    toilets = toi[0]['allpregs']
    handw   = hnd[0]['allpregs']
    risks   = riskys[0]['allpregs']
    rezes   = rez[0]['allreps']
    thins   = thinq[0]['allpregs']
    fats    = fatq[0]['allpregs']
    rezf    = float(rezes)
    toilpc  = 0.0
    handpc  = 0.0
    riskpc  = 0.0
    rezpc   = 0.0
    aapc    = 0.0
    prpc    = 0.0
    try:
      toilpc  = (float(toilets) / totalf) * 100.0
      handpc  = (float(handw) / totalf) * 100.0
      riskpc  = (float(risks) / totalf) * 100.0
      rezpc   = (rezf / totalf) * 100.0
    except ZeroDivisionError, zde:
      pass
    aa      = aarecov[0]['allreps']
    pr      = prrecov[0]['allreps']
    if rezf > 0.0:
      aapc  = (float(aa) / rezf) * 100.0
      prpc  = (float(pr) / rezf) * 100.0
    qs    = range(MONTHS)
    tot   = 0
    dmax  = 0
    for mpos in qs:
      got = orm.ORM.query('pre_table', dict(cits + [('EXTRACT(MONTH FROM report_date) = %s', mpos + 1)]), cols = ['COUNT(*) AS allpregs'])[0]['allpregs']
      qs[mpos]  = got
      tot       = tot + got
      dmax      = max(dmax, got)
    monthavgs = [{'value' : x, 'pc' : 100.0 * (float(x) / tot), 'rpc': 100.0 * (float(x) / dmax)} for x in qs]
    monthavg  = float(tot) / float(MONTHS)
    ls    = range(9)
    tot   = 0
    dmax  = 0
    for mpos in ls:
      got       = orm.ORM.query('pre_table', dict(cits + [('EXTRACT(MONTH FROM lmp) = (EXTRACT(MONTH FROM NOW()) - %s)', len(ls) - (mpos + 1))]), cols = ['COUNT(*) AS allpregs'])[0]['allpregs']
      ls[mpos]  = got
      tot       = tot + got
      dmax      = max(dmax, got)
    tot   = float(tot)
    lmps  = [{'value' : x, 'pc' : 100.0 * (float(x) / tot), 'rpc': 100.0 * (float(x) / dmax)} for x in ls]
    return self.dynamised('pregnancy', mapping = locals(), *args, **kw)

def neat_numbers(num):
  pcs = divided_num(str(num), 3)
  return ','.join(pcs)

def divided_num(num, mx = 3):
  if len(num) < (mx + 1):
    return [num]
  lft = num[0:-3]
  rgt = num[-3:]
  return divided_num(lft) + [rgt]

class ChartMethods(cherrypy.dispatch.Dispatcher):
  def __call__(self, pth):
    gat = re.search(r'/dashboards/(.*)$', pth)
    if gat:
      return super(ChartMethods, self).__call__(gat.group(1).lower())
    return super(ChartMethods, self).__call__(pth.lower())

def wmain(argv):
  if len(argv) < 4:
    sys.stderr.write('%s templatedir staticdir staticpath\r\n' % (argv[0], ))
    return 1
  pth       = os.path.abspath(argv[1])
  bst       = 'base.html'
  stt       = argv[2]
  stp       = argv[3]
  try:
    stp       = settings.STATIC_PATH
  except Exception, e:
    pass
  try:
    bst       = settings.BASE_TEMPLATE
  except Exception, e:
    pass
  thousand  = ThousandCharts(pth, bst, stp, filters = {
    'neat_numbers'  : neat_numbers
  })
  def launch(hst, prt, *args):
    cherrypy.server.socket_host = hst
    cherrypy.server.socket_port = prt
    cherrypy.quickstart(thousand, '/', {
      '/':  {
        'request.dispatch': ChartMethods(),
        'tools.sessions.on':    True,
      },
      # '/static':{
      stp:{
        'tools.staticdir.on':   True,
        'tools.staticdir.root': os.path.abspath(stt),
        # 'tools.staticdir.root': pth,
        'tools.staticdir.dir':  ''
      }
    })
  # thd       = thread.start_new_thread(launch, (None, ))
  launch('0.0.0.0', 8081)

if __name__ == '__main__':
  bottom  = sys.exit(wmain(sys.argv))
