#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import unicodecsv as csv
import xlwt

from datetime import date, timedelta

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rapidsmsrw1000.apps.chws.models import *
from rapidsmsrw1000.apps.ubuzima.models import *
from rapidsmsrw1000.apps.enum import *
import calendar
import json
from django.utils.safestring import SafeString
from dateutil import rrule
from random import randint
import xlsxwriter
from django.db.models import Count


reports = Report.objects.all()

def reports_by_type_by_district():

    filename = "reports_by_type_district.xlsx"

    workbook = xlsxwriter.Workbook(filename, {'constant_memory': True})
    sheet = workbook.add_worksheet('Report')
    
    sheet.write(0,0,"Report Type")
    sheet.write(0,1,"District")
    sheet.write(0,2,"Total")
    
    data = reports.order_by('type__name', 'district__name')
    data_x = data.values('type__name', 'district__name').annotate(total = Count('id'))
    row = 1
    for r in data_x:
      sheet.write(row,0,r['type__name'])
      sheet.write(row,1,r['district__name'])
      sheet.write(row,2,r['total'])
      row = row+1

    workbook.close()

    return True

def anc_by_type_by_district():

    filename = "anc_by_type_district.xlsx"

    workbook = xlsxwriter.Workbook(filename, {'constant_memory': True})
    sheet = workbook.add_worksheet('Report')
    
    sheet.write(0,0,"ANC Type")
    sheet.write(0,1,"District")
    sheet.write(0,2,"Total")
    
    data = Field.objects.filter(type__key__in = ['anc2','anc3', 'anc4'], report__in = reports.filter(type__name = 'ANC')).order_by('type__key', 'district__name')
    data_x = data.values('type__key', 'district__name').annotate(total = Count('id'))
    row = 1
    for r in data_x:
      sheet.write(row,0,r['type__key'])
      sheet.write(row,1,r['district__name'])
      sheet.write(row,2,r['total'])
      row = row+1

    workbook.close()

    return True


