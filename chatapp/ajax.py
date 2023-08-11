from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ajax_request(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        # process input_data here
        result = "You entered: " + input_data
        return HttpResponse(result)