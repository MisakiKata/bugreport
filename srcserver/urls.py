"""srcserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from srclist.views import index, detail, dashboard, users, tracepid
from userlist.views import login, forgot, loginuser, logout, resetpasswd,resetpwd, forgotemail, forgotpwd, forgotset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('index/', index),
    path('users/', users),
    path('detail/<int:page>/', detail),
    path('tracepid/detail/<int:page>/', tracepid),
    path('dashboard/', dashboard),

    path('login/user/', loginuser),           #登陆
    path('login/', login),
    path('forgot/', forgot),                  #忘记密码
    path('forgot/email/', forgotemail),
    path('logout/', logout),                  #退出
    path('resetpasswd/pwd/', resetpasswd),    #密码重置
    path('resetpasswd/', resetpwd),
    path('forgotpwd/', forgotpwd),            #忘记密码修复密码
    path('forgotpwd/resetpwd/<str:code>/', forgotset),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

