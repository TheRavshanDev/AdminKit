from django.shortcuts import render, redirect
from django.views import View
from .models import MainUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        return render(request, 'pages-sign-up.html')

    def post(self, request):
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        mainuser = MainUser.objects.create(
            user=user,
            first_name=request.POST['f-name'],
            last_name=request.POST['l-name'],
        )
        login_terms = authenticate(request, username=user.username, password=user.password)
        login(request, user)
        return redirect('home')

class LoginView(View):
    def get(self, request):
        return render(request, 'pages-sign-in.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            mainuser = MainUser.objects.get(user=user)
            mainuser.login_num += 1
            mainuser.save()
            return redirect('home')
        else:
            messages.error(request, 'User not found!')
            return redirect('signin')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('signin')
