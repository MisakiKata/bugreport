from django.contrib import admin
# from django.contrib.auth.models import User
# Register your models here.
from .models import Userlist
# Userlist = get_user_model()

@admin.register(Userlist)
class Useradmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telephone', 'depart')
    ordering = ('pk',)

admin.site.site_header = 'BUG管理后台'
admin.site.site_title = 'BUG管理后台'