from django.shortcuts import render

# Create your views here.
def homeFunc(request):
    return render(request, "home.html")
