from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, LoginForm


# Shared Views

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def services(request):
	return render(request, 'service.html')

def contact(request):
	return render(request, 'contact.html')

def login_form(request):
	return render(request, 'login.html')

def logout_view(request):
	logout(request)
	return redirect('home')

def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect ('login')
	else:
		form = CustomUserCreationForm()
	return render(request, 'register.html', {'form': form})	


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
