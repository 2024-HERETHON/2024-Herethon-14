from django.forms import TextInput, EmailInput, NumberInput, PasswordInput,FileInput
from django import forms
from .models import CustomUser,MyPage


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password check', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('username','email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': "input idInput",
            }),
            'email': EmailInput(attrs={
                'class': "input emailInput",
            }),
            'password': PasswordInput(attrs={
                'class': "input passwordInput",
                'value':'{{ request.user.password }}',
                }),
        }

class MyPageForm(forms.ModelForm):
    class Meta:
        model=MyPage
        fields = ['profile_image']
        widgets = {
            'profile_image': FileInput(attrs={
                'class': "profile_image",
                'id':"profile_image",
                'style': "display : none;",
                },)
        }