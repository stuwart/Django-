from django.shortcuts import render, HttpResponse, redirect

from app01 import models


# Create your views here.


def depart_list(request):
    '''部门列表'''
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', locals())


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')

    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect('/depart/list')


def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list')


def depart_edit(request, nid):
    if request.method == "GET":
        data = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', locals())
    title = request.POST.get('title')

    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list')


def user_list(request):
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', locals())


def user_add(request):
    if request.method == "GET":
        return render(request, 'user_add.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime,
                                   gender=gender, depart_id=depart_id)

    return redirect('/user/list/')
