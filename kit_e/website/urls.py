from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("login/",views.login_view,name="login"),
    path("signup/",views.sign_up,name="sign-up"),
    path("forgot_password/",views.forgot_password,name="forgot-password"),
    path("",views.home,name="home"),
    #path("send-otp/", views.send_email_otp, name="send-otp"),
    #path("verify-otp/", views.verify_email_otp, name="verify-otp"),
]