from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .ArabicToRoma import convert
# Create your views here.

def index(request):
    if request.POST:
        data = request.POST.get("numeral")
        context = {"data": data}
        print("I'm POST request, hello!")
        return render(request, "my_app/second_index.html", context = context)
    return render(request, "my_app/second_index.html")

@csrf_exempt
def ajax(request):
    print(request.POST)                         #debug
    dt = json.loads(request.POST["pack"])
    print(dt)
    try:                                 #debug
        if int(dt) > 3999:
            return HttpResponse(json.dumps('Too big ;)'))
        elif int(dt) < 1:
            return HttpResponse(json.dumps('Too small ^^,'))
    except:
        pass
    encoded_dt = json.dumps(convert(dt))
    print('encoded ' + encoded_dt)              #debug
    return HttpResponse(encoded_dt)