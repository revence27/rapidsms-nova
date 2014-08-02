#!  /usr/bin/env python

import cherrypy
from jinja2 import Environment, FileSystemLoader
import os, sys, thread
from rapidsmsrw1000.apps.orm import orm
import re
import settings
import subprocess

BMI_MIN = 19
BMI_MAX = 25
orm.ORM.connect(dbname  = 'thousanddays', user = 'thousanddays', host = 'localhost', password = 'thousanddays')
APP_DATA  = {
}

class ThousandDays:
  def __init__(self, pth, bst, stp):
    self.path   = pth
    self.jinja  = Environment(loader = FileSystemLoader(pth))
    self.base   = bst
    self.static = stp

  @cherrypy.expose
  def index(self):
    return self.dynamised('index')

  def app_data(self):
    return APP_DATA

  @cherrypy.expose
  def dynamised(self, chart, mapping = {}, *args, **kw):
    info  = {}
    info.update({
      'base_template' : self.base,
      'static_path'   : self.static
    })
    info.update(self.app_data())
    info.update(kw)
    info.update(mapping)
    return self.jinja.get_template('%s.html' % (chart, )).render(*args, **info)

class ThousandCharts(ThousandDays):
  @cherrypy.expose
  def charts(self):
    return ':-\\'

  @cherrypy.expose
  def delivery(self):
    return self.dynamised('delivery')

  @cherrypy.expose
  def vaccination(self):
    return self.dynamised('vaccination')

  @cherrypy.expose
  def nutrition(self):
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
    return self.dynamised('nutrition', mapping = {
            'nutrition':nut[0],
            'weighed':weighed[0]
    })

  @cherrypy.expose
  def pregnancy(self):
    nat     = orm.ORM.query('pre_table',
      cols      = ['COUNT(*) AS allpregs'],
      annotate  = {
        'coughing':('COUNT(*)', 'ch_bool IS NOT NULL'),
        'diarrhoea':('COUNT(*)', 'di_bool IS NOT NULL'),
        'fever':('COUNT(*)', 'fe_bool IS NOT NULL'),
        'oedema':('COUNT(*)', 'oe_bool IS NOT NULL'),
        'pneumo':('COUNT(*)', 'pc_bool IS NOT NULL'),
        'disab':('COUNT(*)', 'db_bool IS NOT NULL'),
        'cordi':('COUNT(*)', 'ci_bool IS NOT NULL'),
        'necks':('COUNT(*)', 'ns_bool IS NOT NULL'),
        'malaria':('COUNT(*)', 'ma_bool IS NOT NULL'),
        'vomiting':('COUNT(*)', 'vo_bool IS NOT NULL'),
        'stillb':('COUNT(*)', 'sb_bool IS NOT NULL'),
        'jaun':('COUNT(*)', 'ja_bool IS NOT NULL'),
        'hypoth':('COUNT(*)', 'hy_bool IS NOT NULL'),
        'ibibari':('COUNT(*)', 'ib_bool IS NOT NULL')
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
    thins   = weighed.specialise({'(mother_weight_float / ((mother_height_float * mother_height_float) / 10000.0)) < %s': BMI_MIN})
    fats    = weighed.specialise({'(mother_weight_float / ((mother_height_float * mother_height_float) / 10000.0)) > %s': BMI_MAX})
    riskhsh = {'gs_bool IS NOT NULL OR mu_bool IS NOT NULL OR rm_bool IS NOT NULL OR ol_bool IS NOT NULL OR yg_bool IS NOT NULL OR kx_bool IS NOT NULL OR yj_bool IS NOT NULL OR lz_bool IS NOT NULL':''}
    riskys  = nat.specialise(riskhsh)
    rezes   = orm.ORM.query('res_table',
      {},
      cols        = ['COUNT(*) AS allreps'],
    )
    recovs  = rezes.specialise({'mw_bool IS NOT NULL':''})
    aarecov = recovs.specialise({'aa_bool IS NOT NULL':''})
    prrecov = recovs.specialise({'pr_bool IS NOT NULL':''})
    total   = nat[0]['allpregs']
    totalf  = float(total)
    toils   = toi[0]['allpregs']
    hands   = hnd[0]['allpregs']
    toilpc  = 0.0
    handpc  = 0.0
    try:
      toilpc  = (float(toils) / totalf) * 100.0
      handpc  = (float(hands) / totalf) * 100.0
    except ZeroDivisionError, zde:
      pass
    thinc   = thins[0]['allpregs']
    fatc    = fats[0]['allpregs']
    riskc   = riskys[0]['allpregs']
    riskpc  = (float(riskc) / totalf) * 100.0
    rez     = rezes[0]['allreps']
    rezf    = float(rez)
    rezpc   = (rezf / totalf) * 100.0
    aac     = aarecov[0]['allreps']
    aapc    = (float(aac) / rezf) * 100.0
    prc     = prrecov[0]['allreps']
    prpc    = (float(prc) / rezf) * 100.0
    # TODO: do optimisations specialise?
    return self.dynamised('pregnancy', mapping = globals())

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
      print gat.group(1)
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
    APP_DATA  = settings.APP_DATA
  except Exception, e:
    pass
  try:
    stp       = settings.STATIC_PATH
  except Exception, e:
    pass
  try:
    bst       = settings.BASE_TEMPLATE
  except Exception, e:
    pass
  thousand  = ThousandCharts(pth, bst, stp)
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
