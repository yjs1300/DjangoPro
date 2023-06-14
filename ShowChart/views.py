from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,"register.html")
def err(request):
    return render(request,"404.html")
def card(request):
    return render(request,"cards.html")
def forgotpw(request):
    return render(request,"forgot-password.html")
def charts(request):
    return render(request,"charts.html")
