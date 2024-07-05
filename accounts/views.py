from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, MyPageForm, UserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import CustomUser, MyPage
from django.db import IntegrityError



def signup(request): 
    if request.method == 'POST': 
        if request.POST.get('password1') == request.POST.get('password2'): 
            user = get_user_model().objects.create_user( 
                username=request.POST.get('username'), 
                password=request.POST.get('password1'), 
                email=request.POST.get('email'),
            ) 
            print(user)
            auth.login(request, user) 
            return redirect('/') 
        return render(request, 'login.html') 
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

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
'''
@login_required
def mypage(request):
    user = request.user
    mypage_info = MyPage.objects.filter(user=user).first()
    if mypage_info:
        #값 존재할때
        profile_image_message = "이미지를 추가해보세요" if not mypage_info.profile_image else None
    else:
        #존재 안할때
        profile_image_message = "이미지를 추가해보세요"
    return render(request, 'mypage.html', {'mypage_info': mypage_info ,'profile_image_message': profile_image_message})
'''
def mypageUpdate(request):
    user = request.user
    mypage_info = MyPage.objects.filter(user=user).first()
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        mypage_form = MyPageForm(request.POST, request.FILES, instance=mypage_info)
        
        if user_form.is_valid() and mypage_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            mypage_info = mypage_form.save(commit=False)
            mypage_info.user = user
            
            try:
                mypage_info.save()
                user.save()
                update_session_auth_hash(request, user)  # 비밀번호 변경 후 세션 유지
                return redirect('home')
            except IntegrityError:
                user_form.add_error(None, "An error occurred while saving your profile. Please try again.")
    else:
        user_form = UserForm(instance=user)
        mypage_form = MyPageForm(instance=mypage_info)
    
    return render(request, 'profileSetting.html', {'user_form': user_form, 'mypage_form': mypage_form, 'mypage_info': mypage_info})