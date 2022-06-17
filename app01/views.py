from django.shortcuts import render, HttpResponse, redirect
from app01.utils.form import *
from app01 import models
from django import forms


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


def user_model_form_add(request):
    if request.method == "GET":
        form = UserModelForm
        return render(request, 'user_model_form_add.html', locals())

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')

    return render(request, 'user_model_form_add.html', locals())


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def user_edit(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', locals())
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    return render(request, 'user_edit.html', locals())


def pretty_list(request):
    queryset = models.PrettyNum.objects.all()
    return render(request, 'pretty_list.html', locals())


def pretty_add(request):
    if request.method == "GET":
        form = PrettyModelForm
        return render(request, 'pretty_add.html', locals())

    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_add.html', locals())


def pretty_edit(request, nid):
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', locals())
    form = PrettyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_edit.html', locals())

