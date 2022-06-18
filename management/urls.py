from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app01.views import *

urlpatterns = [
    path('', depart_list),
    path('depart/list/', depart_list),
    path('depart/add/', depart_add),
    path('depart/delete/', depart_delete),
    path('depart/<int:nid>/edit/', depart_edit),

    path('user/list/', user_list),
    path('user/add/', user_add),
    path('user/model/form/add/', user_model_form_add),
    path('user/<int:nid>/delete/', user_delete),
    path('user/<int:nid>/edit/', user_edit),

    path('pretty/list/', pretty_list),
    path('pretty/add/', pretty_add),
    path('pretty/<int:nid>/edit/',pretty_edit),



]
