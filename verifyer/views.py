from django.http import HttpResponse
from django.core import serializers
import verify

# Create your views here.
def default(request):
    return HttpResponse('Hello World!')

def test(request):
    url = request.GET.get('url')
    verified_status = verify.verifyLink(url)
    output = serializers.serialize('json', verified_status)
    return HttpResponse(output, mimetype='application/json')
