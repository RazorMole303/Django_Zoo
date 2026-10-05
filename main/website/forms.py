from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'accommodation_type', 'guests', 'full_name', 'email', 'special_requests']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control border-dark', 'id': 'check_in'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control border-dark', 'id': 'check_out'}),
            'accommodation_type': forms.Select(attrs={'class': 'form-select border-dark', 'id': 'accommodation_type'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control border-dark', 'min': 1, 'max': 6}),
            'full_name': forms.TextInput(attrs={'class': 'form-control border-dark', 'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-dark', 'placeholder': 'john@example.com'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control border-dark', 'rows': 3, 'placeholder': 'Dietary requirements, accessibility needs, etc.'}),
        }

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']