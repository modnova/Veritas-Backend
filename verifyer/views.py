from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core import serializers
import verify

# Create your views here.
def test(request):
    url = request.GET.get('url')
    output = verify.verifyLink(url)
    output = serializers.serialize('json', verify.verifyLink(url))
    return HttpResponse(output, mimetype='application/json')
