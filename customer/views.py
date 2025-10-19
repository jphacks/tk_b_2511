from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import AppUserCreationForm, AppLoginForm, appUserUpdateForm
from .models import Customer, AppUser
from django.urls import reverse_lazy

@login_required
def customer_list(request):
    customer = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customer': customer})

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'customer': customer})

@login_required
def customer_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        position = request.POST.get('position')
        notes = request.POST.get('notes')
        hobby = request.POST.get('hobby')
        education = request.POST.get('education')
        born_place = request.POST.get('born_place')
        job = request.POST.get('job')

        Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            position=position,
            notes=notes,
            hobby=hobby,
            education=education,
            birth_date=birth_date,
            born_place=born_place,
            job=job
        )
        return redirect('customer_list')
    return render(request, 'customer/customer_create.html')

def signup(request):
    if request.method == 'POST':
        form = AppUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_list')
    else:
        form = AppUserCreationForm()
    return render(request, 'customer/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_list')
    return render(request, 'customer/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_list(request):
    users = AppUser.objects.all()
    return render(request, 'customer/user_list.html', {'users': users})

@login_required
def user_update(request):
    if request.method == 'POST':
        form = appUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = appUserUpdateForm(instance=request.user)
    return render(request, 'customer/user_update.html', {'form': form})

def dashboard(request):
    appusers = AppUser.objects.all()
    return render(request, 'customer/customer_list.html', {'appusers': appusers})


import requests

def fetch_api_data(request):
    url = "https://v2/everything/data"  # ← 実際のAPIエンドポイントに変更
    headers = {
        "Authorization": "Bearer 4f2cf4fff5b644e2bb652336d8f6eb38",  # 認証が必要な場合
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json() if response.status_code == 200 else {}

    return render(request, "api_result.html", {"data": data})

