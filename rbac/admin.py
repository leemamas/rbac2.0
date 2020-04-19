from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Role)
admin.site.register(PermissionGroup)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display =  ['title','url','action','group']