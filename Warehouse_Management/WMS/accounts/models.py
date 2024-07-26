# accounts/models.py

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    phone_number = PhoneNumberField(unique=True)
    otp = models.CharField(max_length=6, blank=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return str(self.phone_number)
