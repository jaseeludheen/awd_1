from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import auth




def home(request):
    return render(request, 'home/home_page.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('register')  
        else:
            context = {
                'form': form,
            }
            return render(request, 'user/register.html' , context)

  
    else:
        form = RegistrationForm()
        context ={
            'form': form,
        }
    return render(request, 'user/register.html', context)



def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Credentials')
                return render(request, 'user/login.html', {'form': form})
        else:
            messages.error(request, 'Invalid form submission')
            return render(request, 'user/login.html', {'form': form})
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')