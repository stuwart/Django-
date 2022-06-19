from django.shortcuts import render, HttpResponse, redirect
from app01.utils.form import *
from app01.utils.pagination import *
from app01 import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', locals())

    form = LoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        # user = authenticate(username = form.cleaned_data.get('username'),password = form.cleaned_data.get('password'))
        if not admin_object:
            form.add_error('password', '用户名或密码错误！')
            return render(request, 'login.html', locals())
        # 用户名和密码正确，生成cookie和session
        request.session['info'] = {'id': admin_object.id, 'username': admin_object.username}

        return redirect('/pretty/list/')
    return render(request, 'login.html', locals())


def loginout(request):
    request.session.clear()
    return redirect('/login/')
