from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )
    repeat_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )
    age = forms.CharField(
        max_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'Введите свой возраст'})
    )
