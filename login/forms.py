from django import forms
from captcha.fields import ReCaptchaField
class Loginform(forms.Form):
    username=forms.EmailField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    # googlecaptcha=ReCaptchaField()
    captcha=forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class':'captcha-input','placeholder':'Enter code'}))

