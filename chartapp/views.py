from django.shortcuts import render

# Create your views here.

def charthomeFunc(request):
    return render(request,"charthome.html")


