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
def blank(request):
    return render(request,"blank.html")
def card(request):
    return render(request,"cards.html")
def forgotpw(request):
    return render(request,"forgot-password.html")
def tables(request):
    return render(request,"tables.html")
def utilanimal(request):
    return render(request,"utilities-animation.html")
def utilborder(request):
    return render(request,"utilities-border.html")
def utilcolor(request):
    return render(request,"utilities-color.html")
def utilother(request):
    return render(request,"utilities-other.html")
def charts(request):
    return render(request,"charts.html")
