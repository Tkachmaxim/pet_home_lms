from django.urls import path
from users.views import MyLoginView, MySignupView, MyLogoutView


app_name='users'

urlpatterns = [
    path('sign_up/', MySignupView.as_view(), name='signup'),
    path('sign_in/', MyLoginView.as_view(), name='login'),
    path('sign_out/', MyLogoutView.as_view(), name='logout')
    ]
