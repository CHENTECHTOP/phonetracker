from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control bg-dark text-light border-secondary', 'placeholder': 'Придумайте логін'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control bg-dark text-light border-secondary', 'placeholder': 'Придумайте пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control bg-dark text-light border-secondary', 'placeholder': 'Повторіть пароль'})