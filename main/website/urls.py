from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('about/', views.about, name="about"),
    path('visit/', views.visit, name="visit"),
    path('bookings/', views.bookings, name="bookings"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('hotel/', views.hotel, name="hotel" )
]