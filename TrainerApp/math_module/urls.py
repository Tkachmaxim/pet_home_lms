from django.urls import path
from math_module.views import MathInputView

app_name='math_module'

urlpatterns = [
    path('input_data/', MathInputView.as_view(), name='math_input'),
]