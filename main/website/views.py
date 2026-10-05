from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, login_not_required
from .forms import BookingForm, CreateUserForm
from .models import Booking

class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'   # adjust to where your login.html lives
    success_message = "Welcome back, %(username)s! You're now logged in."
    extra_context = {'background_img': 'bat.jpg'}


def home(request):
    return render(request, 'webpages/home.html', {'background_img': 'panda.jpg'})


def about(request):
    return render(request, 'webpages/about.html')


def visit(request):
    if request.method == "POST":
        messages.success(request, "Practice message: no booking has been made.")
        return redirect("")
    return render(request, "webpages/visit.html", {'background_img': 'bat.jpg'})


def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            req_start = book.check_in
            req_end = book.check_out

            cbc = Booking.objects.filter(
                check_in__lt = req_end, check_out__gt = req_start
            ).count()
            if cbc > 2:
                messages.error(request,"Bookings for this room on this date are full, try again another day")
                return render(request, 'webpages/bookings.html', {'form': form, 'background_img': 'koala.jpg'})
            book.save()
            messages.success(request, 'Your booking has been successfully confirmed!')
            return redirect('bookings')
        
    else:
        form = BookingForm()
    return render(request, 'webpages/bookings.html', {'form': form, 'background_img': 'koala.jpg'})

@login_not_required
def register(request):
    if request.user.is_authenticated:
        return redirect('')

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, f"Account created. Welcome, {user.username}!")
            return redirect('')
        messages.error(request, "Please correct the errors below.")
    else:
        form = CreateUserForm()

    return render(request, "registration/register.html", {
        'register_form': form,
        'background_img': 'racoon.jpg',
    })

def logout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You have been logged out. See you soon!")
        return redirect('')

    return render(request, 'registration/logout.html', {'background_img': 'panda.jpg'})

def hotel(request):
     return render(request, 'webpages/hotel.html', {'background_img': 'panda.jpg'})


