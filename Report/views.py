from django.shortcuts import render

# Create your views here.
def report(request):
    render(request, "report.html")
    