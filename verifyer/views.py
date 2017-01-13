from django.http import HttpResponse
import json
import verify

# Create your views here.
def default(request):
    return HttpResponse('Hello World!')

def test(request):
    url = request.GET.get('url')
    verified_status = verify.verifyLink(url)
    output = {'response': verified_status}
    output = json.dumps(output)
    return HttpResponse(output, mimetype='application/json')
