# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.http import HttpResponse
# from django.utils.translation import ugettext_lazy as _
from models import *
import plugins
# Register your models here.
	
# def exportToExcel(modeladmin, request, queryset):
# 	print "Custom Action Execute Success!"
# 	# print "Model:{}".format(modeladmin)
# 	# print "Request:{}".format(request)
# 	# print "QuerySet:{}".format(queryset)
# exportToExcel.short_description = u'导出至Excel'

# class documentListFilter(admin.SimpleListFilter):
# 	title = _(u'')
# 	parameter_name = ''
# 	pass

class RecordInfoInline(admin.TabularInline):
	model = Record

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
	inlines = [RecordInfoInline,]
	list_display = ('document_id', 'location_from', 'valid_code', 'document_code', 'title', 'flag_finished',)
	search_fields = ('document_id', 'title', 'DocumentInfo__opinion_leader','DocumentInfo__location_to',)
	# list_filter = ('time_expired',)
	# fk_fields = ('location_from', 'time_forward', 'location_to', 'time_recycle', 'opinion_leader',)
	actions = ['exportToExcel',]
	date_hierarchy = 'time_expired'

	def exportToExcel(self, request, queryset):
		# for d in queryset:
		# 	print dir(d)
		if queryset.exists():
			self.message_user(request, u'导出成功!')
			response = plugins.exportToExcel(queryset)
			# self.message_user(request, u'导出成功！')
			return response
	exportToExcel.short_description = u'导出至Excel'

# @admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
	list_display = ('document_info', 'time_forward', 'location_to', 'time_recycle', 'opinion_leader',)
	search_fields = ('location_to', 'opinion_leader',)
	# fk_fields = ('location_from',)

# admin.site.register(Document, DocumentAdmin)
# admin.site.register(Record)
admin.site.site_header = '中科院公文后台管理系统'
admin.site.site_title = '中科院公文管理系统'
