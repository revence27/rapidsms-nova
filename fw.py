#!  /usr/bin/env python

import web
import thread

class WebApp:
  ROUTES  = []
  def __init__(self, app, appd):
    self.app  = app
    self.appd = appd
    for k, v in self.__class__.ROUTES:
      self.app.add_mapping(k, v)

  def GET(self):
    return ':o)'

  @classmethod
  def run_service(self, app, appd):
    wa  = self(app, appd)
    return wa.serve()

  @classmethod
  def launch(self, appd, urls = (r'^/$', None)):
    print urls
    f, s  = urls
    app   = web.application((f, s or str(self)), globals())
    thd   = thread.start_new_thread(self.run_service, (app, appd))
    return (app, thd)
