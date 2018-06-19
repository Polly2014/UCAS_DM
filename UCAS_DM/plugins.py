# -*- coding: utf-8 -*-
from django.utils import timezone
from django.http import HttpResponse
from models import *
import time
import xlwt

ISOTIMEFORMAT = '%Y-%m-%d %H:%M'

def timeFormat(time_db):
	return timezone.localtime(time_db).strftime(ISOTIMEFORMAT) if time_db else '-'

def getDetailInfo(documentInfo, recordList):
	DocumentInfo = {
		'id': documentInfo.document_id,
		'title': documentInfo.title,
		'location_from': documentInfo.location_from,
		'time_recieve': timeFormat(documentInfo.time_recieve)
	}
	RecordInfo = {'History':[], 'Current':{}}
	if recordList:
		for record in recordList:
			# print "{}-{}".format(type(record.time_recycle), type(record.time_forward))
			# print "{}-{}".format(timeFormat(record.time_forward), timeFormat(record.time_recycle))
			item = {
				'time_forward': timeFormat(record.time_forward),
				'location_to': record.location_to,
				'time_recycle': timeFormat(record.time_recycle),
				'opinion_leader': record.opinion_leader
			}
			RecordInfo['History'].append(item)
		record = recordList[-1]
		RecordInfo['Current'] = {
			'time_forward': timeFormat(record.time_forward),
			'location_to': record.location_to,
			'time_recycle': timeFormat(record.time_recycle),
			'opinion_leader': record.opinion_leader
		}
	return {'DocumentInfo':DocumentInfo, 'RecordInfo':RecordInfo}

def exportToExcel(documentQuerySet):
	filename = 'DocumentInfo'
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet(u'文档流转信息')
	row_cnt = 0
	for document in documentQuerySet:
		recordQuerySet = Record.objects.filter(document_info=document)
		ws.write(row_cnt, 0, document.document_id)
		ws.write(row_cnt, 1, document.title)
		ws.write(row_cnt, 2, document.location_from)
		ws.write(row_cnt, 3, timeFormat(document.time_recieve))
		if recordQuerySet.exists():
			col_cnt = 4
			for record in recordQuerySet:
				ws.write(row_cnt, col_cnt, record.location_to)
				ws.write(row_cnt, col_cnt+1, timeFormat(record.time_forward))
				ws.write(row_cnt, col_cnt+2, timeFormat(record.time_recycle))
				ws.write(row_cnt, col_cnt+3, record.opinion_leader)
				col_cnt += 4
		row_cnt += 1
		
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename={}.xls'.format(filename)
	wb.save(response)
	return response

