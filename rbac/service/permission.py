def initial_session(request, user):
    '''

    :param request:
    :param user:
    :return:
        request.session.get('permissionsList')
      {
        group.id1: {
            'urls': [permissions__url],
            'actions': [permissions__action]
        },
        group.id2: {
            'urls': [permissions__url],
            'actions': [permissions__action]
        },
    }
    '''

    permissionsList = {}

    permissions = user.roles.all().values('permissions__url', 'permissions__group_id', 'permissions__action').distinct()

    for p in permissions:
        gid = p.get('permissions__group_id')

        if not gid in permissionsList:
            permissionsList[gid] = {
                'urls': [p['permissions__url']],
                'actions': [p['permissions__action']]
            }

        else:
            permissionsList[gid]['urls'].append(p['permissions__url'])
            permissionsList[gid]['actions'].append(p['permissions__action'])

    request.session['permissionsList'] = permissionsList

    permissions = user.roles.all().values('permissions__url',  'permissions__action','permissions__group__title').distinct()

    menu=[]
    for p in permissions:
        if p['permissions__action']=='list':

            menu.append((p['permissions__url'],p['permissions__group__title']))

    print(menu)
    request.session['menu']=menu
