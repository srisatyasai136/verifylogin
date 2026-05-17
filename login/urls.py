from django.urls import path
from . import views
urlpatterns=[
    path("",views.signin,name='signin'),
    path("captcha/",views.captcha_image,name='captcha'),
    path("signup",views.signup,name="signup")
]