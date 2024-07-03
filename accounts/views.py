from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm # 장고에서 제공하는 로그인 폼 사용
from django.contrib.auth import login, logout # 사용자를 로그인, 로그아웃 시키는 역할

<<<<<<< HEAD
# Form 활용
def signup_view(request):
    if request.method == "GET": # 사용자가 회원가입 페이지에 들어갔을 때
        form = SignUpForm() # SignUpForm을 form 변수에 담음
        return render(request, 'accounts/signup.html', {'form' : form}) # form 변수를 가지고 signup.html 페이지를 사용자에게 보여줌
    
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:login') # 회원가입에 성공하면 사용자를 로그인 페이지로 이동시킴
    else:
        return render(request, 'accounts/signup.html', {'form' : form})
    
def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm}) # AuthenticationForm을 사용하여 로그인 폼 생성, form 변수에 담아서 login.html으로 보여줌
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache) # form 변수에 저장된 유저 정보로 로그인시킨 뒤, 사용자를 메인 페이지로 이동시킴
        return redirect('poem:list')
    return render(request, 'accounts/login.html', {'form' : form})

def logout_view(request):
    if request.user.is_authenticated: # 사용자가 로그인 상태라면
        logout(request)
    return redirect('poem:list')
=======
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate



def signup(request): 
    if request.method == 'POST': 
        if request.POST.get('password1') == request.POST.get('password2'): 
            user = User.objects.create_user( 
                username=request.POST.get('username'), 
                password=request.POST.get('password1'), 
                email=request.POST.get('email'),
            ) 
            print(user)
            auth.login(request, user) 
            return redirect('/') 
        return render(request, 'accounts.html') 
    else: 
        
        return render(request, 'accounts.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def accounts(request):
    return render(request, 'home.html')
>>>>>>> ffca27bcd610e69490670e850e05c61fccbdcd20
