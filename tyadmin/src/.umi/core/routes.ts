// @ts-nocheck
import { ApplyPluginsType, dynamic } from 'C:/HeartSoundsSimplified/tyadmin/node_modules/@umijs/runtime';
import { plugin } from './plugin';

const routes = [
  {
    "path": "/xadmin/login",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__UserLayout' */'C:/HeartSoundsSimplified/tyadmin/src/layouts/UserLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "name": "login",
        "path": "/xadmin/login",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__UserLogin' */'C:/HeartSoundsSimplified/tyadmin/src/pages/TyAdminBuiltIn/UserLogin'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "path": "/xadmin/",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__SecurityLayout' */'C:/HeartSoundsSimplified/tyadmin/src/layouts/SecurityLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "path": "/xadmin/",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__BasicLayout' */'C:/HeartSoundsSimplified/tyadmin/src/layouts/BasicLayout'), loading: require('@/components/PageLoading/index').default}),
        "authority": [
          "admin",
          "user"
        ],
        "routes": [
          {
            "name": "Home",
            "path": "/xadmin/index",
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__DashBoard' */'C:/HeartSoundsSimplified/tyadmin/src/pages/TyAdminBuiltIn/DashBoard'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "path": "/xadmin/",
            "redirect": "/xadmin/index",
            "exact": true
          },
          {
            "name": "User",
            "icon": "BarsOutlined",
            "path": "/xadmin/User",
            "routes": [
              {
                "name": "user",
                "path": "/xadmin/User/users",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UsersList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/AutoGenPage/UsersList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "Authentication and Authorization",
            "icon": "BarsOutlined",
            "path": "/xadmin/auth",
            "routes": [
              {
                "name": "permission",
                "path": "/xadmin/auth/permission",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__PermissionList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/AutoGenPage/PermissionList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "group",
                "path": "/xadmin/auth/group",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GroupList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/AutoGenPage/GroupList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "Exhibition",
            "icon": "BarsOutlined",
            "path": "/xadmin/Exhibition",
            "routes": [
              {
                "name": "心音主体",
                "path": "/xadmin/Exhibition/heart_sounds",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__HeartSoundsList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/AutoGenPage/HeartSoundsList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "心音介绍",
                "path": "/xadmin/Exhibition/introduce",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__IntroduceList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/AutoGenPage/IntroduceList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "心音动态部分",
                "path": "/xadmin/Exhibition/dynamic",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__DynamicList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/AutoGenPage/DynamicList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "心音科普",
                "path": "/xadmin/Exhibition/popu_of_science",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__PopuOfScienceList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/AutoGenPage/PopuOfScienceList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "TyadminBuiltin",
            "icon": "VideoCamera",
            "path": "/xadmin/sys",
            "routes": [
              {
                "name": "TyAdminLog",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_sys_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminSysLogList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/TyAdminBuiltIn/TyAdminSysLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "TyAdminVerify",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_email_verify_record",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminEmailVerifyRecordList' */'C:/HeartSoundsSimplified/tyadmin/src/pages/TyAdminBuiltIn/TyAdminEmailVerifyRecordList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "passwordModify",
            "path": "/xadmin/account/change_password",
            "hideInMenu": true,
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__ChangePassword' */'C:/HeartSoundsSimplified/tyadmin/src/pages/TyAdminBuiltIn/ChangePassword'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'C:/HeartSoundsSimplified/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          }
        ]
      },
      {
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'C:/HeartSoundsSimplified/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'C:/HeartSoundsSimplified/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
    "exact": true
  }
];

// allow user to extend routes
plugin.applyPlugins({
  key: 'patchRoutes',
  type: ApplyPluginsType.event,
  args: { routes },
});

export { routes };
