# import django.contrib.auth
# from django.contrib.auth import authenticate, login
# from django.shortcuts import redirect
# from Login.forms import UserForm
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from . models import Member
import json



def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    # login 요청이 들어왔을때
    elif request.method == "POST":
        m_id = request.POST.get('account')
        m_pwd = request.POST.get('password')
        
        # DB에서 아이디 목록만 가져온다.
        m_id_list = Member.objects.values_list('m_id', flat=True)
        context={}
        
        # print(m_id_list)
        for i in range(len(m_id_list)):
            if m_id == m_id_list[i]: # 아이디가 데이터베이스에 존재한다면
                user = Member.objects.get(m_id=m_id)
                # print('m_pwd :', m_pwd)
                # print('user.m_pwd :', user.m_pwd)
                if (m_pwd == user.m_pwd): # 비밀번호가 맞는지 확인하고
                    request.session['user'] = user.m_id  # 맞는다면 세션을 생성한다.
                    print('로그인 성공') 
                    return redirect('/') # 로그인 성공시 홈으로 이동함.
                
                else: # 비밀번호가 일치하지 않는다면 
                    context.clear()
                    context["pwderror"] = "비밀번호가 일치하지 않습니다."
                    return render(request, "login.html",context)
                
            else: # 아이디가 존재하지 않는다면
                context["iderror"] = "아이디가 존재하지 않습니다."
                
        return render(request, "login.html", context)
        
        # if m_id_list == m_id:
        
        # M_check = Member.objects.filter(m_id=m_id)
        # P_check = Member.objects.filter(m_pwd=m_pwd)
        
        # # 오류 
        # if M_check.count() == 0 or P_check.count() == 0:
        #     return render(request,"error.html") 
            
            
        
        # else:
        #     user = Member.objects.get(m_id=m_id)
        #     # print('m_pwd :', m_pwd)
        #     # print('user.m_pwd :', user.m_pwd)
        #     if (m_pwd == user.m_pwd ):
        #         request.session['user'] = user.m_id
                
        #         print('로그인 성공')
        #         return redirect('/') # 로그인 성공시 홈으로 이동함.
        #     else:
        #         print('로그인 실패')
       
        # return render(request, "login.html",)
                 
                   
                 
# 회원가입기능 구현 중

def signup(request): 
    # if request.method =="GET":
    #     return render(request,'login.html')
    
    # elif request.method == "POST": 
    #     m_id = request.POST.get('account')
    #     m_name = request.POST.get('username') 
    #     m_pwd = request.POST.get('password')  
    #     m_email = request.POST.get('email')
        
    if request.method == "POST": 
        m_id = request.POST.get('account')
        m_name = request.POST.get('username') 
        m_pwd = request.POST.get('password')  
        m_email = request.POST.get('email') 
        
        if not (m_id and m_pwd):
           pass
            
        else:
            user = Member(m_id = m_id, m_name=m_name ,m_pwd = m_pwd, m_email = m_email)
            user.save()
        
        return redirect("/login") # 가입 성공하면 로그인 페이지로 리다이렉트

# 로그아웃
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect("/")

# 아이디 중복확인 창 띄우기
def checkpop(request):
    if request.method == "GET": 
        return render(request, "check.html")
    
    
# 아이디 중복확인 후   
def checkid(request):
    #   useid = request.GET.get('idcheck')
    result = []
    
    if request.method =="GET":
        id = request.GET['idcheck']
        # print(Member.objects.get(m_id=id))
        # context =[]
        # db 관련은 try except 사용하기    
        try:
            Member.objects.get(m_id=id)
            print("중복됨")
            dic = {'result':"true"}
            result.append(dic)
        
        except Member.DoesNotExist:
            print("중복없음")
            dic = {'result':"fall"}
            result.append(dic)

    return HttpResponse(json.dumps(result), content_type="application/json")  
   
   
    # return JsonResponse(context)
          # if Member.objects.get(m_id=id):
        #     print("중복됨")
        #     dic = {'result':"true"}
        #     result.append(dic)
            
        # else:
        #     print("중복없음")
        #     dic = {'result':"fall"}
        #     result.append(dic)  
            
          #   중복이라면




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