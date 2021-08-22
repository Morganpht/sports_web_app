from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# Create your views here.

def homepage(request):
    return render(request=request, template_name="main/homepage.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
			user.profile.gender = form.cleaned_data.get('gender')
			user.save()
			username = form.cleaned_data.get('username')
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			messages.success(request, f"Registration successful: {username}" )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")

def profile(request, username):
	user = get_object_or_404(User, username=username)
	user_age = calculate_age(user.profile.date_of_birth)
	return render(request=request, template_name="main/profile.html", context={"user":user, "user_age":user_age})