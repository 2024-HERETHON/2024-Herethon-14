from django import forms
from django.contrib.auth import get_user_model # 사용할 user model을 가져옴
from django.contrib.auth.forms import UserCreationForm # 장고에서 제공하는 기본 유저 생성 폼

class SignUpForm(UserCreationForm):
    class Meta():
        model = get_user_model() # 회원가입에 사용할 모델
        fields = ['username', 'email'] # 회원가입 시 사용자로부터 입력받을 필드