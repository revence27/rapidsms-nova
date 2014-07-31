#!  /usr/bin/env python

import cherrypy
from lxml import html as templates
import os, sys, thread
from rapidsmsrw1000.apps.orm import orm
import re
import subprocess
import web

BMI_MIN = 19
BMI_MAX = 25
orm.ORM.connect(dbname  = 'thousanddays', user = 'thousanddays', host = 'localhost', password = 'thousanddays')

class ThousandDays:
  def __init__(self, pth):
    self.path = pth

  @cherrypy.expose
  def index(self):
    return file(os.path.join(self.path, 'html', 'index.html'))

class ThousandCharts(ThousandDays):
  @cherrypy.expose
  def charts(self):
    return ':-\\'

  def process_template(self, pth, mapping, query):
    ans = ''
    with file(pth) as f:
      doc = templates.fromstring(f.read())  # TODO: cache templates
      for cle, val in mapping:
        fin = doc
        dem = cle
        dat = val
        if not hasattr(cle, '__iter__'):
          dem = [cle]
        for prc in dem:
          if hasattr(prc, '__call__'):
            fin = prc(fin)
          else:
            fin = fin.cssselect(prc)
            if type(fin) == type([]):
              try:
                fin = fin[0]
              except IndexError:
                raise Exception, (u'No children in "%s" over %d.' % (prc, len(fin)))
        if not (type(dat) in [type(x) for x in ['', u'', 0, 0L, 1.6182]]):
          if type(dat) == type((object, 'method', ['args'])):
            dat = getattr(dat[0], dat[1])(*dat[2:])
          else:
            raise Exception, ('How to process "%s" (%s) of "%s"?' % (dat, type(dat), cle))
        for pc in (fin if type(fin) == type([]) else [fin]):
          pc.text  = unicode(dat)
      ans = templates.tostring(doc)
    return ans

  @cherrypy.expose
  def dynamised(self, chart = 'pregnancy', mapping = [], query = None):
    return self.process_template(os.path.join(self.path, 'html', '%s.html' % (chart, )), mapping, query)

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
    return self.dynamised('nutrition', mapping = [
      ('#layer_118', neat_numbers(nut[0]['breast'])),
      ('#layer_34', neat_numbers(nut[0]['notbreast'])),
      ('#layer_1121', neat_numbers(nut[0]['unknown'])),
      ('#layer_108', neat_numbers(bir[0]['hour1'])),
      # ('#layer_79', neat_numbers(bir[0]['hour1'])),
      ('#layer_152', '%.2f%%' % ((weighed[0]['short'] / weighed[0]['mums']) * 100.0, ))
    ])

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
    return self.dynamised(mapping = [
      ('#layer_150 a', neat_numbers(nat[0]['allpregs'])),
      ('#risks69', ('%.1f%%' % (prpc, ))),
      ('#risks66', ('%.1f%%' % (aapc, ))),
      ('#risks65', neat_numbers(aac)),
      ('#risks78', neat_numbers(prc)),
      ('#layer_129', neat_numbers(riskc)),
      ('#layer_89', ('%.1f%%' % (riskpc, ))),
      ('#layer_89_0', neat_numbers(rez)),
      ('#layer_75', ('%.1f%%' % (rezpc, ))),
      ('#COUGHING24 strong', neat_numbers(nat[0]['coughing'])),
      ('#DIARRHEA33 strong', neat_numbers(nat[0]['diarrhoea'])),
      ('#FEVER12 strong', neat_numbers(nat[0]['fever'])),
      ('#MALARIA09 strong', neat_numbers(nat[0]['malaria'])),
      ('#VOMITING18 strong', neat_numbers(nat[0]['vomiting'])),
      ('#STILLBORN21 strong', neat_numbers(nat[0]['stillb'])),
      ('#EDEMA13 strong', neat_numbers(nat[0]['oedema'])),
      ('#JAUNDICE09 strong', neat_numbers(nat[0]['jaun'])),
      ('#PNEUMONIA21 strong', neat_numbers(nat[0]['pneumo'])),
      ('#DISABILITY21 strong', neat_numbers(nat[0]['disab'])),
      ('#HYPOTHEMIA21 strong', neat_numbers(nat[0]['hypoth'])),
      ('#CLEFTPALATE21 strong', neat_numbers(nat[0]['ibibari'])),
      ('#CORDINFECTION strong', neat_numbers(nat[0]['cordi'])),
      ('#NECKSTIFFNESS strong', neat_numbers(nat[0]['necks'])),
      ('#layer_12289 strong', neat_numbers(hands)),
      ('#layer_10985 strong', neat_numbers(toils)),
      ('#layer_21', neat_numbers(fatc)),
      ('#layer_90', neat_numbers(thinc)),
    ])

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
  if len(argv) < 3:
    return wmain(argv + ['0.0.0.0:8081'])
  hst, prt  = argv[2].split(':', 2)
  pth       = os.path.abspath(argv[1])
  thousand  = ThousandCharts(pth) # ThousandDays(pth)
  def launch(hst, prt, *args):
    cherrypy.server.socket_host = hst
    cherrypy.server.socket_port = prt
    cherrypy.quickstart(thousand, '/', {
      '/':  {
        'request.dispatch': ChartMethods(),
        'tools.sessions.on':    True,
        'tools.staticdir.on':   True,
        # 'tools.staticdir.root': os.path.join(os.path.abspath(argv[1]), 'static'),
        'tools.staticdir.root': pth,
        'tools.staticdir.dir':  ''
      }
    })
  # thd       = thread.start_new_thread(launch, (None, ))
  launch(hst, int(prt))
  apres     = os.getenv('POST_THOUSAND', 'exit;')
  subprocess.call([apres, 'http://%s/' % (argv[2], )])

if __name__ == '__main__':
  bottom  = sys.exit(wmain(sys.argv))
