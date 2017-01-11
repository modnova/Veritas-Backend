from django.shortcuts import render
# veritas/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import verify
# Create your views here.
def test(request):
    if request.method == 'POST':
       output = verify.verifyLink();
       return HttpResponse(output, content_type="text/plain")
