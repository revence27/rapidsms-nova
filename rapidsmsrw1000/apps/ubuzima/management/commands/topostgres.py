from django.core.management.base import BaseCommand
# from ubuzima.models import Report, Reminder, ReminderType, TriggeredAlert
# from ubuzima.models import *
from rapidsmsrw1000.apps.ubuzima.models import *
from django.conf import settings
# from ..reporters.models import Reporter
import urllib2
import time
import datetime
import re, sys
from optparse import make_option
from rapidsmsrw1000.apps.thoureport.reports.reports import *
from rapidsmsrw1000.settings import THE_DATABASE as postgres, __DEFAULTS

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

  def __str__(self):
    return '%s TESTER' % (self.conver[self.autos.type.pk],)

class Command(BaseCommand):
    help = 'Copy the messages (and reports), with all supporting data (locations, facilities ...), over to the Postgres DB.'

    def handle(self, **options):
      curz  = postgres.cursor()
      reps  = Report.objects.order_by('-date')[0:20000]
      convr = BasicConverter()
      print 'Starting conversion ...'
      cpt   = float(reps.count())
      pos   = 0
      maxw  = 80
      for rep in reps:
        fps = float(pos + 1)
        pct = (fps / cpt) * 100.0
        gap = ' ' * max(0, (int(((fps / cpt) * float(maxw))) - len('100.0%') - len(str(pos + 1)) - 2))
        pad = ' ' * maxw
        osp = OldStyleReport(rep, curz, convr)
        rsp = ('%d %s%3.1f%%%s' % (pos + 1, gap, pct, pad))
        sys.stdout.write('\r' + rsp[0:maxw])
        sys.stdout.flush()
        if not osp.convert():
          raise Exception, str(osp)
        pos = pos + 1
      print 'Done converting ...'
      curz.close()
      postgres.commit()
