from django.shortcuts import render, HttpResponse, redirect
from app01.utils.form import *
from app01.utils.pagination import *
from app01 import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    data_dict = {}
    search_data = request.GET.get('q', '')
    p = request.GET.get('p', 1)
    if search_data:
        data_dict['mobile__contains'] = search_data

    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('-level')

    # paginator = Paginator(queryset, 10)
    # try:
    #     pages = paginator.page(p)
    # except PageNotAnInteger:
    #     pages = paginator.page(1)
    # except EmptyPage:
    #     pages = paginator.page(paginator.num_pages)
    # has_next: 判断是否有下一页
    # has_previous: 判断是否有上一页
    # objects_list: 分页之后的数据列表
    # next_page_number: 下一页页码
    # previous_page_number: 上一页页码
    # number: 当前页（属性）
    # paginator: paginator对象

    page_object = Pagination(request, queryset)

    context = {
        "search_data": search_data,

        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'pretty_list.html', context)


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
