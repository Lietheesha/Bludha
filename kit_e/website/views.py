from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from .models import CustomUser,CustomUserManager
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .utils import generate_otp
import random

# Create your views here.
# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return JsonResponse({
                "success": False,
                "message": "All fields are required"
            })

        user = authenticate(request, email=email, password=password)
        

        '''  if not user.is_email_verified:
                return JsonResponse({
                    "success": False,
                    "message": "Please verify your email first"
                })'''
        if user is not None: 
            auth_login(request, user)
            return JsonResponse({
                "success": True,
                "message": "Login successful"
            })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid username or password"
            })

    return render(request, "authentication/login.html")


# ---------------- SIGN UP ----------------
def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "Email already registered"})

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        return JsonResponse({"success": True, "redirect": "/login/"})

    ''' # Generate OTP
        otp = generate_otp()
        user.email_otp = otp
        user.otp_expires_at = timezone.now() + timedelta(minutes=5)
        user.save()

        # Send email
        send_mail(
           "Your OTP",
            f"Your OTP is {otp}",
            "noreply@bludha.com",
            [email],
        )

        # Store email in session
        request.session["verify_email"] = email '''
    return render(request, "authentication/signup.html")

# ---------------- FORGOT PASSWORD (BASIC) ----------------
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            return JsonResponse({
                "success": False,
                "message": "Email is required"
            })

        if not CustomUser.objects.filter(email=email).exists():
            return JsonResponse({
                "success": False,
                "message": "No account found with this email"
            })

        # Later you can add email reset logic here
        return JsonResponse({
            "success": True,
            "message": "Password reset link will be sent"
        })

    return render(request, "authentication/forgot_password.html")

'''
# ---------------- OTP GENERATING ----------------
def send_email_otp(request):
    if "verify_email" not in request.session:
        return redirect("/signup/")

    return render(request, "authentication/otp.html")

# ---------------- VERIFY OTP ----------------
def verify_email_otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        email = request.session.get("verify_email")

        try:
            user = CustomUser.objects.get(email=email)
        except:
            return JsonResponse({"status": "error"})

        if user.email_otp == otp and timezone.now() <= user.otp_expires_at:
            user.is_email_verified = True
            user.email_otp = None
            user.otp_expires_at = None
            user.save()

            del request.session["verify_email"]

            return JsonResponse({"status": "verified"})

        return JsonResponse({"status": "invalid"})

'''

# ---------------- HOME ----------------
def home(request):
    return render(request, "app/home.html")

