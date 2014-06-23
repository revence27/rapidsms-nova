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
