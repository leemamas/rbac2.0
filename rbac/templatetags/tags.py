from django import template

register=template.Library()


@register.inclusion_tag('rbac/menu.html')
def get_menu(request):
    menu=request.session['menu']

    return {'menu':menu}