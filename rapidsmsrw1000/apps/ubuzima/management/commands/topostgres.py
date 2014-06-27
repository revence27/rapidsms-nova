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
    option_list = BaseCommand.option_list + (
        make_option('-n', '--number',
                    # action='store_true',
                    dest='number',
                    default=5000,
                    help='Number of reports to transfer.'),
        )

    def handle(self, *args, **options):
      curz  = postgres.cursor()
      cpt   = int(options.get('number', 5000))
      seen  = []
      qry   = ThouReport.query('report_logs', {}, cols = ['indexcol'])
      for ix in range(qry.count()):
        seen.append(qry[ix]['indexcol'])
      print ('Already got %d ...' % (len(seen),))
      reps  = Report.objects.exclude(id__in = seen).order_by('-date')[0:cpt]
      convr = BasicConverter()
      print ('Starting conversion (%d) ...' % (cpt,))
      cpt   = float(reps.count())
      pos   = 0
      maxw  = 80
      stbs  = set()
      for rep in reps:
        fps = float(pos + 1)
        pct = (fps / cpt) * 100.0
        gap = ' ' * max(0, (int(((fps / cpt) * float(maxw))) - len('100.0%') - len(str(pos + 1)) - 2))
        pad = ' ' * maxw
        osp = OldStyleReport(rep, curz, convr)
        rsp = ('%d %s%3.1f%%%s' % (pos + 1, gap, pct, pad))
        sys.stdout.write('\r' + rsp[0:maxw])
        sys.stdout.flush()
        gat             = osp.convert()
        suc, thid, tbn  = gat
        if not any([suc, thid]):
          raise Exception, str(gat)
        stbs.add(tbn)
        pos = pos + 1
        postgres.commit()
      print 'Done converting ...'
      print 'List of secondary tables:'
      for tbn in stbs:
        print tbn
      curz.close()
      postgres.commit()
      postgres.close()
