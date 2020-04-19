from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import re
from rbac.service.permission import *


def index(request):
    return render(request,'index.html')

def login(request):

    if request.method == 'POST':

        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        user = User.objects.filter(name=user, pwd=pwd).first()
        if user:
            request.session['user_id']=user.pk

            initial_session(request,user)

            return HttpResponse('login success!')
        else:
            msg='error!'

    return render(request, 'login.html', locals())


def user(request):
    users=User.objects.all()
    permission=Permission(request.actions)
    return render(request, 'users.html', locals())

def user_add(request):
    return HttpResponse('user add！')

def user_edit(request,id):

    print('edit', id)
    return HttpResponse('user edit！')

def user_delete(request,id):
    print('delete',id)
    return HttpResponse('user delete！')


def role(request):
    return HttpResponse('roles views!')


def role_add(request):
    return HttpResponse('role add!')

class Permission(object):
    def __init__(self,actions):
        self.actions=actions

    def list(self):
        return 'list' in self.actions

    def add(self):
        return 'add' in self.actions

    def edit(self):
        return 'edit' in self.actions

    def delete(self):
        return 'delete' in self.actions
