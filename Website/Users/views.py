from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm#, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return  redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    #u_form = UserUpdateForm()
    #p_form = ProfileUpdateForm()

    context = {
        'u_form' : None,
        'p_form' : None
    }

    return render(request, 'users/profile.html', context)


#messages.debug
#messages.info
#messages.success
#messages.warning
#messages.error