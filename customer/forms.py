from django import forms
from .models import AppUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class AppLoginForm(AuthenticationForm):
    username = forms.CharField(label="ユーザ名", max_length=150)
    password = forms.CharField(label="パスワード" , widget=forms.PasswordInput)

class appUserUpdateForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'phone')
        labels = {
            'username': 'ユーザ名',
            'email': 'メールアドレス',
            'phone': '電話番号',
        }

