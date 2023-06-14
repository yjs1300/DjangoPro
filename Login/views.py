# import django.contrib.auth
# from django.contrib.auth import authenticate, login
# from django.shortcuts import redirect
# from Login.forms import UserForm
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User

def signup(request): 
    if request.method =="GET":
        return render(request,'signup.html')
    elif request.method == "POST": 
        username = request.POST.get['username', None] 
        password = request.POST.get['password', None]  
        email = request.POST.get['email', None]
        name = request.POST.get['name', None]
        re_password = request.POST.get['re_password',None]
        res_data = {}
        if not (username and password and re_password):
            res_data["error"] = "모든 값을 입력해야 합니다."
        if password != re_password:
            res_data["error"] = "비밀번호가 일치하지 않습니다."
        else:
            user = User(username = username, password = make_password(password))
            user.save()

# Create your views here.
# authenticate() django의 인증기능
# def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid(): # 데이터 유효성 검사
#             form.save() 
#             username = form.cleaned_data.get("username") # cleaned_data 는 Form 의 안에서 정의한 필드에 값에 대해서만 리턴
#             raw_password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=raw_password)  # 사용자 인증
#             login(request,user) # 로그인 기능
#             return redirect('home')
            
#         else:
#             form = UserForm()
#         return render(request, 'signup.html', {'form':form})       
