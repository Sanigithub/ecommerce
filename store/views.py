from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render (request, 'shop.html', context)


def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        return redirect('/signin/')
    context = {'form':form}
    return render (request, 'signup.html', context)

    
def signin(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    context = {'form':form}
    return render (request, 'signin.html', context)
