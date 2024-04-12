from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'users/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')