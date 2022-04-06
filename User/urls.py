from django.urls import path
from . import views
from .views import RegisterView, ForgetPasswordView, SubmitEmailUsernameView,LogoutView,LoginView

app_name='User'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('passwordforget/', ForgetPasswordView.as_view(), name='forgetpassword'),
    path('pfcode/', SubmitEmailUsernameView.as_view(), name='emailusername'),
]