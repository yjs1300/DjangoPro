from django.shortcuts import render

# Create your views here.
# 지도 보여주기 
def showmap(request):
    return render(request, "map.html")

