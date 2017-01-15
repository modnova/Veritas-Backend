from django.http import HttpResponse
import json
import verify

# Create your views here.


def default(request):
    return HttpResponse('Hello World!')


def test(request):
    url = request.GET.get('url')
    verified_status = verify.main(url)
    output = json.dumps(verified_status)
    return HttpResponse(output, content_type='application/json')
