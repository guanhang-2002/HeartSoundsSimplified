import logging

from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import FormView, RedirectView

from HeartSoundsSimplified import utility
from HeartSoundsSimplified.utility import send_email, generate_code
from User.form import RegisterForm, LoginForm, ForgetPasswordForm, SubmitEmailUsername
from User.models import Users

logger = logging.getLogger('file')
maillogger = logging.getLogger('mail')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    # @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(False)
            user.is_active = True
            user.save(True)
            content = """<p>感谢您注册HeartSounds数据库</p>"""
            send_email(
                emailto=[
                    user.email,
                ],
                title='HeartSounds',
                content=content)
            logout(self.request)
            # Delete(user.username)
            logger.info(f'user{user.username}register')
            return redirect(reverse('User:login'))
        else:
            return self.render_to_response({
                'form': form
            })


# 暂时删除Uesr
def Delete(username):
    Users.objects.filter(username=username).delete()


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'
    login_ttl = 60 * 60 * 24  # 一天的时间
    # @method_decorator(sensitive_post_parameters('password'))
    # @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST, request=self.request)
        if self.request.session.get('has_login'):
            return render(self.request, 'index.html', context={'repeatloginmessage': '你不能重复登录'})
        elif form.is_valid():
            active_user = form.get_user()
            auth.login(self.request, active_user)
            self.request.session.set_expiry(0)
            self.request.session['has_login'] = True
            logger.info(f'{self.request.user.username} login')
            return super(LoginView, self).form_valid(form)
        else:
            return self.render_to_response({
                'form': form
            })



class LogoutView(RedirectView):
    url = '/'

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logger.info(f'user{self.request.user.username}logout')
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class ForgetPasswordView(FormView):
    form_class = ForgetPasswordForm
    template_name = 'forget_password.html'

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data['email']
            code = cache.get(email)

            if code != form.cleaned_data['code']:
                return HttpResponse('验证码错误')
            else:
                user = Users.objects.filter(email=email).get()
                logger.info(f'{user}repeatpassword-code:{code}')
                user.password = make_password(form.cleaned_data["new_password2"])
                user.save()
                return HttpResponseRedirect('/')
        else:
            return self.render_to_response({'form': form})


class SubmitEmailUsernameView(View):

    def post(self, request):
        form = SubmitEmailUsername(request.POST)
        if not form.is_valid():
            return HttpResponse("请检查是否填写正确")
        else:
            try:
                has_user=Users.objects.get(form.cleaned_data['username'])
                has_email=Users.objects.get(form.cleaned_data['email'])
                if not has_user and not has_email:
                    raise ValueError('邮箱或用户名不存在')
            except Exception as e:
                maillogger.error(e)
            to_email = form.cleaned_data["email"]
            code = generate_code()
            utility.send_verify_email(to_email, code)
            utility.set_code(to_email, code)

        return redirect(reverse('User:forgetpassword'))

    def get(self, request):
        form = SubmitEmailUsername()
        return render(request, 'submitEmailUsername.html', locals())
