# encoding: UTF-8
from django.core.management.base import BaseCommand
# from ubuzima.models import Report, Reminder, ReminderType, TriggeredAlert
# from ubuzima.models import *
from rapidsmsrw1000.apps.ubuzima.models import *
from django.conf import settings
# from ..reporters.models import Reporter
import urllib2
import time as times
import datetime
import re, sys, os
from optparse import make_option
from rapidsmsrw1000.apps.thoureport.reports.reports import *

class Command(BaseCommand):
    help = 'Copy the messages (and reports), with all supporting data (locations, facilities ...), over to the Postgres DB.'
    option_list = BaseCommand.option_list + (
        make_option('-t', '--type',
                    # action='store_true',
                    dest    = 'type',
                    default = None,
                    help    = 'Report type ID to privilege.'),
        make_option('-n', '--number',
                    # action='store_true',
                    dest    = 'number',
                    default = 5000,
                    help    = 'Number of reports to transfer.'),
        make_option('-b', '--background',
                    action='store_true',
                    dest    = 'background',
                    default = False,
                    help    = u'Dæmonise.'),
        make_option('-r', '--repeat',
                    action='store_true',
                    dest    = 'repeat',
                    default = False,
                    help    = 'When done, do again.'),
        make_option('-f', '--force',
                    action='store_true',
                    dest    = 'force',
                    default = False,
                    help    = 'Only works if -d is on. Also delete those that are being transferred.'),
        make_option('-d', '--delete',
                    action  = 'store_true',
                    dest    = 'delete',
                    default = False,
                    help    = 'Delete Report.objects.filter(id__in = [Already transferred]).delete().')
        )

    def handle(self, *args, **options):
      def gun():
        from rapidsmsrw1000.settings import NOVA_DEFAULTS
        REPORTS_TABLE = NOVA_DEFAULTS['REPORTS']
        postgres  = psycopg2.connect(
            database = NOVA_DEFAULTS['NAME'],
                user = NOVA_DEFAULTS['USER'],
            password = NOVA_DEFAULTS['PASSWORD'],
                host = NOVA_DEFAULTS['HOST']
        )
        ThouReport.postgres = postgres
        once  = True
        while once:
          once  = self.single_handle(REPORTS_TABLE, postgres, *args, **options) and options.get('repeat', not once)
        postgres.close()
      if options.get('background'):
        chp = os.fork()
        if chp:
          print 'Background:', chp
          return
        gun()
      else:
        gun()

    def single_handle(self, tbn, pgc, *args, **options):
      cpt   = int(options.get('number', 5000))
      force = options.get('force', False)
      qry   = ThouReport.query(tbn,
        {'NOT transferred' : ('',)},
        cols        = ['former_pk', 'indexcol'],
        migrations  = [
          ('former_pk', 0),
          ('transferred', (True, 'BOOLEAN NOT NULL DEFAULT FALSE'))
        ]
      )
      dsiz  = qry.count()
      seen  = set()
      upds  = []
      deler = options.get('delete', False)
      if deler:
        upds  = []
      for ix in range(dsiz):
        row   = qry[ix]
        if not row: break
        ixnum = row['former_pk']
        act   = 'Loaded'
        if deler:
          try:
            it  = Report.objects.get(id = ixnum)
            it.delete()
          except Exception, e:
            pass
          upds.append(str(row['indexcol']))
        act   = 'Deleted'
        sys.stdout.flush()
        seen.add(ixnum)
      # print 'Updating deletion status ...',
      ThouReport.store(tbn,
        {'indexcol': upds, 'transferred': True}
      )
      # print '... done.'
      curz  = pgc.cursor()
      reps  = Report.objects.exclude(id__in = seen).order_by('-date')
      gat = options.get('type', None)
      if gat:
        reps  = reps.filter(type_id = gat)
      tot   = reps.count()
      if not tot: return False
      cpt   = min(tot, cpt)
      reps  = reps[0:cpt]
      # print ('Already got %d of %d, now moving %d ...' % (len(seen), tot, cpt))
      convr = BasicConverter({'transferred':True} if deler and force else {})
      cpt   = float(cpt)
      pos   = 0
      maxw  = 80
      # batch = ThouReport.batch()
      batch = ThouReport.batch()
      stbs  = set()
      sttm  = times.time()
      for rep in reps:
        fps = float(pos + 1)
        pct = (fps / cpt) * 100.0
        gap = ' ' * max(0, (int(((fps / cpt) * float(maxw))) - len('100.0%') - len(str(pos + 1)) - 2))
        ctm = times.time() - sttm
        dlt = datetime.timedelta(seconds = int(ctm * (cpt / fps)))
        eta = datetime.datetime.now() + dlt
        pad = ((' %s ' % (str(dlt), )) + (' ' * maxw))
        osp = OldStyleReport(rep, curz, convr)
        if not options.get('background'):
          rsp = ('%d %s%3.1f%%%s' % (pos + 1, gap, pct, pad))
          sys.stdout.write('\r' + rsp[0:maxw])
          sys.stdout.flush()
        # gat             = osp.convert(batch = batch)
        gat             = osp.convert()
        suc, thid, tbn  = gat
        if not any([suc, thid]):
          raise Exception, str(gat)
        if deler and force:
          rep.delete()
        stbs.add(tbn)
        pos = pos + 1
        pgc.commit()
      batch.run()
      # print 'Done converting ...'
      # print 'List of secondary tables:'
      # for tbn in stbs:
      #   print tbn
      curz.close()
      pgc.commit()
      return True
