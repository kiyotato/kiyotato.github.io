from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def user_id(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'User_bio.html', {'user':user})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:user_id")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="register.html", context={"register_form":form})
    


