from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


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

@login_required
def setting(request):
    user = request.user
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            user.userImage.delete()
            user.userImage = image
        user.save()
    return render(request, 'profileSetting.html', {'userImg': user.userImage})