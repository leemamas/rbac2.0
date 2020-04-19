
from django.contrib import admin
from django.urls import path,re_path
from rbac.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('', index),
    path('user/', user),
    path('user/add/', user_add),
    re_path('user/edit/(\d+)/', user_edit),
    re_path('user/delete/(\d+)/', user_delete),
    path('role/', role),
    path('role/add/', role_add),
]
