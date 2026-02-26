from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

User = get_user_model()

def index(request):
    return render(request, 'index.html')

def register_page(request):
    return render(request, 'registration.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return redirect('registration')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('registration')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Enter a valid email address")
            return redirect('registration')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('registration')


        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone=phone
        )

        messages.success(request, "Account created successfully")
        return redirect('login')

def login_page(request):
    return render(request, 'login.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if not email or not password:
            messages.error(request, "Email and password are required")
            return redirect('login')

        user_obj = User.objects.filter(email=email).first()
        if user_obj is None:
            messages.error(request, "Invalid credentials")
            return redirect('login')

        user = authenticate(username=user_obj.username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        messages.error(request, "Invalid credentials")
        return redirect('login')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

def chatdashboard(request):
    return render(request, 'chatdashboard.html')