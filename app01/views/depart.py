from django.shortcuts import render, HttpResponse, redirect
from app01.utils.form import *
from app01.utils.pagination import *
from app01 import models


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
