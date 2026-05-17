from django import forms
from captcha.fields import ReCaptchaField
# from django_recaptcha.fields import ReCaptchaField
# from django_recaptcha.widgets import ReCaptchaV2Checkbox
class Loginform(forms.Form):
    username=forms.EmailField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    googlecaptcha=ReCaptchaField()
    # googlecaptcha=ReCaptchaField(
    #     widget=ReCaptchaV2Checkbox
    # )
    captcha=forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class':'captcha-input','placeholder':'Enter code'}))

