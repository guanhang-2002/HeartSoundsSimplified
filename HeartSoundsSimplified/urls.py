"""HeartSoundsSimplified URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from tyadmin_api.views import AdminIndexView
import Index.urls
urlpatterns = [
    path('',include('Index.urls',namespace='Index')),
    path('user/',include('User.urls',namespace='User')),
    path('exhibition/',include('Exhibition.urls',namespace='Exhibition')),
    re_path('^xadmin/.*', AdminIndexView.as_view()),
    path('api/xadmin/v1/', include('tyadmin_api.urls')),
]
