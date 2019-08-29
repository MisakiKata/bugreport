from django.shortcuts import render, redirect
from .models import vulnlist, trace_esc
from userlist.models import Userlist
import html

# Create your views here.

def index(request):
    if request.session.get('is_login') != '1':
        return redirect('/login')
    else:
        assets = vulnlist.objects.all()
        return render(request, 'index.html', {'assets':assets})


def detail(request, page):
    if request.session.get('is_login') != '1':
        return redirect('/login/')
    id = vulnlist.objects.get(id=page).id
    title = vulnlist.objects.get(id=page).title
    name = vulnlist.objects.get(id=page).name
    developuser = vulnlist.objects.get(id=page).developuser
    level = vulnlist.objects.get(id=page).level
    status = vulnlist.objects.get(id=page).status
    text = vulnlist.objects.get(id=page).vulntext
    vulntext = html.unescape(text)
    putuser = vulnlist.objects.get(id=page).putuser
    data_time = vulnlist.objects.get(id=page).data_time
    Repairplan = vulnlist.objects.get(id=page).Repairplan

    vulndata = trace_esc.objects.filter(vulnid=page)

    return render(request, 'detail.html', locals())


def dashboard(request):
    if request.session.get('is_login') != '1':
        return redirect('/login/')
    total = vulnlist.objects.count()
    newvul = vulnlist.objects.filter(status=1).count()
    nowdeal = vulnlist.objects.filter(status=2).count()
    processed = vulnlist.objects.filter(status=3).count()
    complete = vulnlist.objects.filter(status=4).count()
    overrule = vulnlist.objects.filter(status=5).count()

    o_rate = round(newvul / total * 100)
    un_rate = round(nowdeal / total * 100)
    bd_rate = round(processed / total * 100)
    bu_rate = round(complete / total * 100)
    up_rate = round(overrule / total * 100)


    Lowrisk = vulnlist.objects.filter(level=3).count()
    Intermediaterisk = vulnlist.objects.filter(level=2).count()
    Highrisk = vulnlist.objects.filter(level=1).count()
    ignore = vulnlist.objects.filter(status=5).count()


    return render(request, 'dashboard.html', locals())


def users(request):
    if request.session.get('is_login') != '1':
        return redirect('/login/')
    assets = Userlist.objects.all()
    return render(request, 'users.html', locals())
    pass


def tracepid(request, page):
    if request.session.get('is_login') != '1':
        return redirect('/login/')
    if request.method == "POST":
        track_desc = request.POST.get('track_desc')
        id = request.POST.get('id')
        vstate = request.POST.get('vstate')
        developuser = request.session.get('username','')
        if track_desc:
            trace_esc.objects.create(data=track_desc, vulnid=page, developuser=developuser)
            vulnerable = vulnlist.objects.filter(id=id)
            vulnerable.update(status = vstate)
            redirect('/detail/'+str(page))
        else:
            STATUS = {
                '1': '新提交',
                '2': '正在处理',
                '3': '已修复，待验证',
                '4': '修复完成',
                '5': '已驳回',
            }
            track_desc = STATUS[vstate]
            trace_esc.objects.create(data=track_desc, vulnid=page, developuser=developuser)
            vulnerable = vulnlist.objects.filter(id=id)
            vulnerable.update(status=vstate)
            return redirect('/detail/'+str(page))

    return redirect('/detail/'+str(page))
