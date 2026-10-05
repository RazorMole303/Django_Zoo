from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'accommodation_type', 'check_in', 'check_out', 'guests', 'created_at')
    list_filter = ('accommodation_type', 'check_in', 'check_out')
    search_fields = ('full_name', 'email')
    ordering = ('-created_at',)