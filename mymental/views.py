from django.shortcuts import render, redirect
import time
from .models import Rating_data, To_do_list
from datetime import date
from .forms import Rating_dataForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Creates the session for the user using the auth_login alias
            auth_login(request, user)
            return redirect("rating_page")
    else:
        form = AuthenticationForm()
    return render(request, 'login_page.html', {"form": form})


@login_required
def rating_page(request):
    submitted = False
    checker_day = date.today()
    if Rating_data.objects.filter(date=checker_day, user=request.user).exists():
        submitted = True
    current_date = time.strftime("%d-%m-%Y")
    context = {
        'date': current_date,
        'submitted': submitted,
        'rating_data': Rating_dataForm()
    }
    return render(request, 'rating_page.html', context)


@login_required
def statistics_page(request):
    rating_data = Rating_data.objects.filter(user=request.user)[:7]
    mood_sum = 0
    prod_sum = 0
    times = 0
    mood_last7 = Rating_data.objects.filter(
        user=request.user).values("mood_rating").order_by('-id')[:7]
    prod_last7 = Rating_data.objects.filter(
        user=request.user).values("productivity_rating").order_by('-id')[:7]
    for item in mood_last7:
        mood_sum += int(item['mood_rating']) or 0
        times += 1
    for item in prod_last7:
        prod_sum += int(item['productivity_rating']) or 0
    if times != 0:
        mood_avg = mood_sum / times
        prod_avg = prod_sum / times
    else:
        mood_avg = '-'
        prod_avg = '-'
    context = {
        'rating_data': rating_data,
        'mood_avg': mood_avg,
        'prod_avg': prod_avg,
    }
    return render(request, 'statistics_page.html', context)


@login_required
def get_statistics(request):
    if request.method == "POST":
        rating_data = Rating_dataForm(request.POST)
        if rating_data.is_valid():
            instance = rating_data.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('statistics_page')
    else:
        rating_data = Rating_dataForm()
    return render(request, 'rating_page.html', {'rating_data': rating_data})


def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.form_valid() if hasattr(form, 'form_valid') else form.save()
            auth_login(request, user)
            messages.success(request, "✅ account created successfully!")
            return redirect("rating_page")
    else:
        form = RegisterForm()
    return render(request, 'register_page.html', {"form": form})


def log_out(request):
    # Ends the user session
    logout(request)
    return redirect('login')


def to_do_list_page(request):
    if request.method == "POST":
        task_title = request.POST.get('task_title')
        user = request.user
        if task_title != "" and len(task_title) <= 24:
            To_do_list.objects.create(task_title=task_title, user=user)
        else:
            messages.error(request, "Task title is either empty or too big⚠️")
        return redirect('to_do_list')
    tasks = To_do_list.objects.filter(user=request.user).order_by('created')
    context = {
        'tasks': tasks
    }
    return render(request, 'to_do_list_page.html', context)


def to_do_list_checkbox(request, task_id):
    task = To_do_list.objects.get(id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('to_do_list')


def task_delete_view(request, task_id):
    task = To_do_list.objects.get(id=task_id)
    task.delete()
    return redirect('to_do_list')
