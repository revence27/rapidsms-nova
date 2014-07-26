#!  /usr/bin/env python

import cherrypy
import os, sys, thread
import re
import subprocess
import web

class ThousandDays:
  def __init__(self, pth):
    self.path = pth

  @cherrypy.expose
  def index(self):
    return ':o)'

class ThousandCharts(ThousandDays):
  @cherrypy.expose
  def charts(self):
    return ':-\\'

  @cherrypy.expose
  def dynamised(self, chart = 'pregnancy', mapping = {}):
    return file(os.path.join(self.path, 'html', '%s.html' % (chart, )))

  @cherrypy.expose
  def delivery(self):
    return self.dynamised('delivery')

  @cherrypy.expose
  def vaccination(self):
    return self.dynamised('vaccination')

  @cherrypy.expose
  def nutrition(self):
    return self.dynamised('nutrition')

  @cherrypy.expose
  def pregnancy(self):
    return self.dynamised(mapping = {
      '#layer_150 a:first':120
    })

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
  def launch(*args):
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
  launch()
  apres     = os.getenv('POST_THOUSAND', 'exit;')
  subprocess.call([apres, 'http://%s/' % (argv[2], )])

if __name__ == '__main__':
  bottom  = sys.exit(wmain(sys.argv))
