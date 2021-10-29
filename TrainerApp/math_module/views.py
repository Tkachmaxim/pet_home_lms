from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class MathInputView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'mathtrainer.html')



