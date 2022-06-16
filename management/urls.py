from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app01.views import *

urlpatterns = [
    path('',depart_list),
    path('depart/list/', depart_list),
    path('depart/add/', depart_add),
    path('depart/delete/', depart_delete),
    path('depart/<int:nid>/edit/', depart_edit),


    path('user/list/',user_list),
    path('user/add/', user_add),
    # path('user/delete/', user_delete),
    # path('user/<int:nid>/edit/', user_edit),
]
