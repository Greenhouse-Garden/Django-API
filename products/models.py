from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    image_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_at']   
        
        
    
        