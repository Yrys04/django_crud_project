from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Убираем декоратор login_required
def register(request):
    if request.method == 'POST':
        # Используем вашу кастомную форму RegisterForm вместо UserCreationForm
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Автоматическая авторизация после регистрации
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Регистрация прошла успешно!')
                return redirect('car_list')
        else:
            messages.error(request, 'Исправьте ошибки в форме')
    else:
        form = RegisterForm()
    return render(request, 'cars/register.html', {'form': form})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_create(request):
    if request.method == "POST":
        marka = request.POST.get('marka')
        model = request.POST.get('model')
        gos_number = request.POST.get('gos_number')
        Car.objects.create(marka=marka, model=model, gos_number=gos_number)
        return redirect('car_list')
    return render(request, 'cars/car_create.html')

def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car.marka = request.POST.get('marka')
        car.model = request.POST.get('model')
        car.gos_number = request.POST.get('gos_number')
        car.save()
        return redirect('car_list')
    return render(request, 'cars/car_update.html', {'car': car})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_delete.html', {'car': car})