from django.shortcuts import render, HttpResponse, redirect
from app01.utils.form import *
from app01.utils.pagination import *
from app01 import models


def admin_list(request):
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['username__contains'] = search_data

    queryset = models.Admin.objects.filter(**data_dict)

    # 分页 常规组件
    page_object = Pagination(request, queryset)
    queryset = page_object.page_queryset
    page_string = page_object.html
    # context = {
    #     'queryset': page_object.page_queryset,
    #     'page_string': page_object.html,
    # }

    return render(request, 'admin_list.html', locals())


def admin_add(request):
    title = '添加管理员'
    if request.method == "GET":
        form = AdminModelForm
        return render(request, 'add.html', locals())

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'add.html', locals())


def admin_edit(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        msg = '数据不存在'
        return render(request, 'error.html', locals())
    title = '编辑管理员'

    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'change.html', locals())

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', locals())


def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()

    if not row_object:
        return redirect('/admin/list/')
    title = '重置密码 - {}'.format(row_object.username)

    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change.html', locals())

    form = AdminResetModelForm(data=request.POST, instance=row_object)

    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', locals())
