from django.contrib import admin

# Register your models here.

from .models import appname

@admin.register(appname)
class applistadmin(admin.ModelAdmin):
    list_display = ('name', 'abbrename', 'developuser', 'researchuser', 'appurl')
    ordering = ('pk',)


