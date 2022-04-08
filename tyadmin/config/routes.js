[
    {
        name: 'Home',
        path: '/xadmin/index',
        icon: 'dashboard',
        component: './TyAdminBuiltIn/DashBoard'
    },
    {
        path: '/xadmin/',
        redirect: '/xadmin/index',
    },
    {
        name: 'User',
        icon: 'BarsOutlined',
        path: '/xadmin/User',
        routes:
        [
            {
                name: 'user',
                path: '/xadmin/User/users',
                component: './AutoGenPage/UsersList',
            }
        ]
    },
    {
        name: 'Authentication and Authorization',
        icon: 'BarsOutlined',
        path: '/xadmin/auth',
        routes:
        [
            {
                name: 'permission',
                path: '/xadmin/auth/permission',
                component: './AutoGenPage/PermissionList',
            },
            {
                name: 'group',
                path: '/xadmin/auth/group',
                component: './AutoGenPage/GroupList',
            }
        ]
    },
    {
        name: 'Exhibition',
        icon: 'BarsOutlined',
        path: '/xadmin/Exhibition',
        routes:
        [
            {
                name: '心音主体',
                path: '/xadmin/Exhibition/heart_sounds',
                component: './AutoGenPage/HeartSoundsList',
            },
            {
                name: '心音介绍',
                path: '/xadmin/Exhibition/introduce',
                component: './AutoGenPage/IntroduceList',
            },
            {
                name: '心音动态部分',
                path: '/xadmin/Exhibition/dynamic',
                component: './AutoGenPage/DynamicList',
            },
            {
                name: '心音科普',
                path: '/xadmin/Exhibition/popu_of_science',
                component: './AutoGenPage/PopuOfScienceList',
            }
        ]
    },
    {
        name: 'TyadminBuiltin',
        icon: 'VideoCamera',
        path: '/xadmin/sys',
        routes:
        [
            {
                name: 'TyAdminLog',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_sys_log',
                component: './TyAdminBuiltIn/TyAdminSysLogList'
            },
            {
                name: 'TyAdminVerify',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_email_verify_record',
                component: './TyAdminBuiltIn/TyAdminEmailVerifyRecordList'
            }
        ]
    },
    {
        name: 'passwordModify',
        path: '/xadmin/account/change_password',
        hideInMenu: true,
        icon: 'dashboard',
        component: './TyAdminBuiltIn/ChangePassword',
    },
    {
        component: './404',
    },
]
