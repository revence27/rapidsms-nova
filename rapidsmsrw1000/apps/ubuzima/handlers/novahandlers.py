#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsmsrw1000.apps.thoureport.messages.rapid1000messages import *
from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler

class NovaHandler(KeywordHandler):
  """Intercepting the normal handler, cleanly."""

  def is_fine(msg, rep):
    msg = self.msg
    pid = rep.msg.entries.get('patient_id')
    lox = self.location_info(rep)
    lox['reporter_pk']    = msg.connection.contact.pk,
    lox['reporter_phone'] = msg.connection.identity,
    lox['patient_pk']     = self.__get_patient_pk()
    rep.save(('%s_table' % (rep.code, )).lower(), **lox)

  def has_errors(msg):
    # TODO: Can be cleaner, like the old views.
    self.respond('\n'.join(terr.errors))

  def is_unknown(uk):
    pass

  # TODO:
  # Consider the message field classes' declared default.
  # Also:
  # 1.  Facilities.
  # 2.  Health workers
  # 3.  Locations
  # 4.  Patients
  def handle(self, text):
    ThouMessage.parse_report(
      text,
      is_fine,
      REPORT_SET,
      error_handler = has_errors,
      unknown_handler = is_unknown
    )
    return self.classic_handle()

  def __get_detail(self, dt):
    return self.msg.get(dt)

  def __get_patient_pk(self):
    got = self.__get_detail('national_id')
    raise Exception, got

  def __get_village_pk(self):
    return self.connection.contact.village.pk

  def __get_hc_pk(self):
    return self.connection.contact.health_centre.pk

  def __get_district_pk(self):
    return self.connection.contact.district.pk

  def __get_sector_pk(self):
    return self.connection.contact.sector.pk

  def __get_province_pk(self):
    return self.connection.contact.province.pk

  def __get_cell_pk(self):
    return self.connection.contact.cell.pk

  def location_info(self, rep):
    ans                     = {}
    ans['village_pk']       = self.__get_village_pk()
    ans['health_center_pk'] = self.__get_hc_pk()
    ans['district_pk']      = self.__get_district_pk()
    ans['sector_pk']        = self.__get_sector_pk()
    ans['province_pk']      = self.__get_province_pk()
    ans['cell_pk']          = self.__get_cell_pk()
    return ans
