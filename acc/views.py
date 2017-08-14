from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.encoding import python_2_unicode_compatible
from django.views import View
from django.contrib.auth.decorators import login_required


@python_2_unicode_compatible
class Index(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'acc/index.html')
