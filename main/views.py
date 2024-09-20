from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from item.models import *
from .forms import SignupForm
from django.contrib.auth import logout 

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'pages/index.html', {
        'categories': categories,
        'items': items,
        
    })

def contact(request):
    return render(request, 'pages/contact.html')

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
            form = SignupForm()    

    form = SignupForm()

    return render(request, 'pages/signup.html',{
        'form': form
    })


@login_required
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('index') 


# for user info page
@login_required
def logged_user(request):
    user = request.user  # Get the logged-in user
    return render(request, 'pages/logged_user.html', {'user': user})