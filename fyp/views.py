from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Product
from .register_form import RegisterForm
from django.contrib import messages
from rest_framework import permissions
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.

class Home(APIView):
	def get(self, request):
		queryset=Product.objects.all()
		return render(request,'chamb/home.html', {'products':queryset})


class Login(APIView):
	def get(self, request):
		return render(request, 'chamb/login.html')

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		error_message='Invalid Username or Password'
		return render(request, 'chamb/login.html', {'error_message': error_message})

class Signup(APIView):
	def get(self, request):
		return render(request, 'chamb/signup.html')

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/user-login')
		messages.error(request, form.errors)
		return render(request, 'chamb/signup.html', {'form': form})

class SingleProduct(APIView):
	def get(self, request, obj_id):
		queryset=Product.objects.get(id=obj_id)
		if request.user.is_authenticated:
			return render(request, 'chamb/productpage.html', {'query':queryset})
		return redirect('/user-login')


class AboutUs(APIView):
	def get(self, request):
		return render(request, 'chamb/about-us.html')

class Logout(APIView):
	def get(self, request):
		logout(request)
		return redirect('/')

class ContactUs(APIView):
	def get(self, request):
		return render(request, 'chamb/contact-us.html')