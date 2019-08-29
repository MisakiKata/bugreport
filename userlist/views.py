from django.shortcuts import render, redirect
from .models import Userlist, resetuser
from .sendemail import sendmail
import time
from django.conf import settings
# Create your views here.


TIME_ZONE = settings.TIME_ZONE

def login(request):
    if request.session.get('is_login') == '1':
        return redirect('/index')
    return render(request, 'my-login/index.html')


def loginuser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email.strip() and password:
            try:
                user = Userlist.objects.get(email=email)
            except:
                message = '用户不存在'
                return render(request,'my-login/index.html', locals())
            if user.password == password:
                request.session['is_login'] = '1'
                request.session['user.id'] = user.id
                request.session['username'] = user.username
                return redirect('/index/')
            else:
                message = '密码不正确'
                return render(request, 'my-login/index.html', locals())
        else:
            message = '请输入正确格式的用户名和密码'
            return render(request, 'my-login/index.html', locals())
    return redirect('/login/')



def forgot(request):
    return render(request, 'my-login/forgot.html')


def forgotemail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = Userlist.objects.filter(email=email)
        except:
            message = '用户不存在'
            return render(request, 'my-login/forgot.html', locals())
        sendmail(email)
        message = "邮件发送成功"
        return render(request, 'my-login/forgot.html', locals())
    message = "请求失败"
    return render(request, 'my-login/forgot.html', locals())


def resetpwd(request):
    name = request.user
    return render(request, 'resetpasswd.html', locals())


def logout(request):
    if request.session.get('is_login') != '1':
        return redirect('/login')
    request.session.flush()
    return redirect("/login/")


def resetpasswd(request):
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "POST":
        oldpwd = request.POST.get('oldpwd')
        newpwd = request.POST.get('newpwd')
        newpwd_confirmation = request.POST.get('newpwd_confirmation')
        if newpwd == newpwd_confirmation:
            try:
                username = request.session.get('username','')
                user = Userlist.objects.get(username=username)
            except:
                message = '修改密码失败'
                return render(request, 'resetpasswd.html', locals())
            if user.password == oldpwd:
                if user.password == newpwd:
                    message = '新密码和旧密码一致'
                    return render(request, 'resetpasswd.html', locals())
                else:
                    u = Userlist.objects.filter(username=username)
                    u.update(password = newpwd)
                    message = '密码修改成功'
                    return render(request, 'resetpasswd.html', locals())
            else:
                message = '密码修改失败'
                return render(request, 'resetpasswd.html', locals())
        else:
            message = '新密码输入不一致'
        return render(request,'resetpasswd.html', locals())

    return redirect('/resetpasswd')


def forgotpwd(request):
    return render(request, 'my-login/reset.html')


def forgotset(request, code):
    if request.method == "GET" and code:
        return render(request, 'my-login/reset.html')
    elif request.method == "GET" and not code:
        message = '验证链接无效'
        return render(request, 'my-login/forgot.html', locals())
    if request.method == "POST":
        password = request.POST.get('password')
        try:
            user = resetuser.objects.get(resetcode=code)
        except:
            message = '验证链接无效'
            return render(request, 'my-login/forgot.html', locals())
        if time.time() >= user.failtime:
            message = "链接失效，请重新验证"
            return render(request, 'my-login/forgot.html', locals())
        else:
            username = user.resetuser
            u = Userlist.objects.filter(email=username)
            u.update(password = password)
            resetuser.objects.filter(resetuser=username).update(resetcode = '')
            message = '修改成功，请重新登陆'
            return render(request, 'my-login/reset.html', locals())
    message = '请输入正确格式的密码'
    return render(request, 'my-login/reset.html', locals())