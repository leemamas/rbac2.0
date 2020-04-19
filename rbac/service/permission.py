

def initial_session(request,user):
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
    # permissions = user.roles.all().values('permissions__url').distinct()
    #
    # permissionsList = []
    # for permission in permissions:
    #     permissionsList.append(permission['permissions__url'])
    #
    # request.session['permissionsList'] = permissionsList

    permissionsList = {}

    permissions = user.roles.all().values('permissions__url','permissions__group_id','permissions__action').distinct()

    for p in permissions:
        gid=p.get('permissions__group_id')
        url=p.get('permissions__url')
        action=p.get('permissions__action')
        # print(gid)
        # print(url )
        # print(action)
        if not gid in permissionsList:
            permissionsList[gid]={
                'urls':[p['permissions__url']],
                'actions':[p['permissions__action']]
            }

        else:
            permissionsList[gid]['urls'].append(p['permissions__url'])
            permissionsList[gid]['actions'].append(p['permissions__action'])

    # print(permissionsList)
    request.session['permissionsList'] = permissionsList

