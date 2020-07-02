from django.shortcuts import render
from . forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse("Your account was inactive.")

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'register.html',{'user_form': user_form, 'registered': registered})



@login_required
def special(request):
    return render(request, 'special.html', {'output':"You are logged in!!"})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')
    
@login_required
def payment(request):
    return render(request, 'payment.html')

@login_required
def home(request):
    return render(request, 'core/special.html')