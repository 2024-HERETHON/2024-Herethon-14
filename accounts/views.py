from django.shortcuts import render

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