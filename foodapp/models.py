from django.db import models

class Registration(models.Model):

    CATEGORY_CHOICES = [
        ('startup_founder', 'Startup Founder'),
        ('investor', 'Investor'),
        ('student', 'Student'),
        ('professional', 'Professional'),
    ]
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"
    
from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

