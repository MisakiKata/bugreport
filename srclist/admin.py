from django.contrib import admin

# Register your models here.
from .models import vulnlist

@admin.register(vulnlist)
class vulnadmin(admin.ModelAdmin):

    list_display = ('data_time', 'title', 'name', 'developuser', 'level', 'status', 'putuser')
    ordering = ('-pk',)

