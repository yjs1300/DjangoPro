import django.contrib.auth
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from Login.forms import UserForm


# Create your views here.
# authenticate() django의 인증기능
def signup(request):
    if request.method == "POST":
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request,user) # 로그인 기능
            return redirect('home.html')
            
        else:
            form = UserForm()
        return render(request, 'signup.html', {'form':form})            