#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsmsrw1000.apps.thoureport.messages.rapid1000messages import *
from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler

class NovaHandler(KeywordHandler):
  """Intercepting the normal handler, cleanly."""

  # TODO: Consider the message field classes' declared default.
  # Also:
  # 1.  Facilities.
  # 2.  Health workers
  # 3.  Locations
  # 4.  Patients
  def handle(self, text):
    try:
      rep = ThouMessage.parse(text)
      msg = self.msg
      pid = rep.msg.entries.get('patient_id')
      lox = self.location_info(rep)
      lox['reporter_pk']    = msg.connection.contact.pk,
      lox['reporter_phone'] = msg.connection.identity,
      lox['patient_pk']     = None  # TODO.
      rep.save(('%s_table' % (rep.code, )).lower(), **lox)
    except ThouMsgError, terr:
      self.respond('\n'.join(terr.errors))
    return self.classic_handle()

  def location_info(self, rep):
    ans = {}
    ans['village_pk']       = None  # TODO.
    ans['health_center_pk'] = None  # TODO.
    ans['district_pk']      = None  # TODO.
    ans['sector_pk']        = None  # TODO.
    ans['province_pk']      = None  # TODO.
    ans['cell_pk']          = None  # TODO.
    return ans
