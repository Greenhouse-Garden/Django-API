''' Users models file'''
#django/django
from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    postalCode = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.IntegerField(blank=True, null=True) 
    
    cc_number = CardNumberField(null=True)
    cc_expiry = CardExpiryField(null=True)
    cc_code = SecurityCodeField(null=True)
       
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at  = models.DateTimeField(auto_now_add=True)
    
    
    
    

    class Meta:
        ordering = ['created_at']   
        
    def __str__(self):
        return self.user.get_full_name()
        