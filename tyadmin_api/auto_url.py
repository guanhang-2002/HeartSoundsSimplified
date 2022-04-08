from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('users', auto_views.UsersViewSet)
    
router.register('permission', auto_views.PermissionViewSet)
    
router.register('group', auto_views.GroupViewSet)
    
router.register('content_type', auto_views.ContentTypeViewSet)
    
router.register('heart_sounds', auto_views.HeartSoundsViewSet)
    
router.register('introduce', auto_views.IntroduceViewSet)
    
router.register('dynamic', auto_views.DynamicViewSet)
    
router.register('popu_of_science', auto_views.PopuOfScienceViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    