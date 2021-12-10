from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class EventAdmin(ImportExportModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ('name',)


class NotifyAdmin(ImportExportModelAdmin):
    list_display = ('email', 'phone')
    search_fields = ('email', 'phone', 'event',)


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Notify, NotifyAdmin)
