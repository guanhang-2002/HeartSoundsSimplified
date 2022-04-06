from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import UploadView, HeartSoundsDemonstrate, HeartSoundsList

app_name='Exhibition'

urlpatterns = [
    path('upload/', login_required(UploadView.as_view()), name='upload'),
    path('file_detail/<int:id>/', login_required(HeartSoundsDemonstrate.as_view()), name='file_detail'),
    path('file_list/<int:page>/', HeartSoundsList.as_view(), name='file_list'),
    path('file_download/<int:id>', views.download, name='file_download')
]