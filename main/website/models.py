from django.db import models
from django.conf import settings

class Booking(models.Model):
    ACCOMMODATION_CHOICES = [
        ('red_panda', 'Red Panda Lodge (£150/night)'),
        ('panda_suite', 'Panda Sanctuary Suite (£220/night)'),
        ('safari_cabin', 'Wildlife Safari Cabin (£180/night)'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    accommodation_type = models.CharField(max_length=50, choices=ACCOMMODATION_CHOICES)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=2)
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_accommodation_type_display()} ({self.check_in})"

class tasks(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="posted_tasks")
    # Meta will allow us to change the data before we either input or output the data from the database
    class Meta:
        ordering = ["-created_at", "-pk"]
    # Return the title if we peek at the data before fetching
    def __str__(self):
        return self.title;