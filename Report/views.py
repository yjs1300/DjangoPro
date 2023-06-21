from django.shortcuts import render
import os

# Create your views here.
def report(request):
    print(os.getcwd())
    return render(request,"report.html")
    