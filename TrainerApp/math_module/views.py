from django.shortcuts import render
from django.views import View


class MathInputView(View):
    def get(self, request):
        return render(request, 'mathtrainer.html')


