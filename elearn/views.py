from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, LoginForm
from .models import TakenQuiz, Profile, Quiz, Question, Answer, Learner, CustomUser, Course, Notes, Announcement, Tutorial 

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
	return redirect('login')

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


# Admin Views

def dashboard(request):
    learner = CustomUser.objects.filter(is_learner=True).count()
    instructor = CustomUser.objects.filter(is_instructor=True).count()
    course = Course.objects.all().count()
    users = CustomUser.objects.all().count()
    context = {'learner':learner, 'course':course, 'instructor':instructor, 'users':users}

    return render(request, 'dashboard/admin/home.html', context)
