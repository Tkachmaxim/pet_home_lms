from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from users.forms import RegisterUserForm


class MySignupView(CreateView):
    form_class = RegisterUserForm
    success_url = '/users/sign_in'
    template_name = r'users/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = r'users/login.html'

class MyLogoutView(LogoutView):
    template_name = 'index.html'
