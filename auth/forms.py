# Email as username
from django import forms

from emailusernames.forms import EmailUserCreationForm
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class RegistrationForm(EmailUserCreationForm):
    captcha = CaptchaField(label="Cosa vedi scritto qui sotto?")
    class Meta:
    	model = User
        fields = ("username", "email", "password1", "password2", "captcha")