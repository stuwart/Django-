from django.shortcuts import render, HttpResponse, redirect
from app01.utils.form import *
from app01.utils.pagination import *
from app01 import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
