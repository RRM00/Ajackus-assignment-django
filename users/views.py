from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created please login    {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.htm', {'form': form})

def profile(request):
    return render(request, 'users/profile.htm')

# Create your views here.
