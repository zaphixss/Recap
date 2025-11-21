from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

INPUT_CLASS = (
    "peer w-full rounded-xl border border-zinc-200 dark:border-zinc-800 "
    "bg-white dark:bg-zinc-900 px-3.5 py-2.5 pr-11 text-[15px] outline-none "
    "transition focus-visible:ring-2 focus-visible:ring-indigo-500 "
    "focus-visible:ring-offset-2 dark:focus-visible:ring-offset-zinc-950"
)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                "class": INPUT_CLASS,
                "placeholder": "you@example.com",

            }
        )
        
    )

    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": INPUT_CLASS,
                "placeholder": "Ada Lovelace",
            }
        )
        
    )

    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
               "class": INPUT_CLASS,
               "placeholder": "At least 8 characters",
            }
        )

    )

    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
               "class": INPUT_CLASS,
               "placeholder": "At least 8 characters",
            }
        )
        
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                "class": INPUT_CLASS,
                "placeholder": "you@example.com",

            }
        )
        
    )
     
     
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
               "class": INPUT_CLASS,
               "placeholder": "At least 8 characters",
            }
        )

    )