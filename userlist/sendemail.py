#coding:utf-8


import os
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import hashlib
from .models import resetuser
import time

os.environ['DJANGO_SETTINGS_MODULE'] = 'srcserver.settings'
salt = settings.SECRET_KEY
host = settings.VERIFY_HOST


def sendmail(email):
    semail = settings.EMAIL_HOST_USER               #发件人邮箱
    codes = code(email)
    verfiyurl = host +'/forgotpwd/resetpwd/'+str(codes)          #密码修改地址
    html_text = """
        <h3>密码重置</h3>
        <p>请访问如下地址来重置密码，有效期为30分钟</p>地址：<a href=%s>%s</a>
    """  %(verfiyurl, verfiyurl)

    subject, from_email, to = '密码重置邮件', semail, email  #标题  发件人  收件人
    text_content = '密码重置：请访问如下地址来重置密码，地址：<a href=%s>%s</a>' %(verfiyurl, verfiyurl)
    html_content = html_text
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def code(email):
    m = hashlib.md5()
    m.update((email+'|'+salt+'|'+str(time.time())).encode('utf-8'))
    code = m.hexdigest()
    failtime = time.time()+1800
    resetuser.objects.create(resetuser=email, resettime=time.time(), resetcode=code, failtime=failtime)
    return m.hexdigest()
