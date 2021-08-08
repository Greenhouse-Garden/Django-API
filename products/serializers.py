from rest_framework import serializers
from products.models import Products


""" class ProductsSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=70, allow_blank=False)
    description = serializers.CharField(max_length=255, allow_blank=True)
    price = serializers.IntegerField()
    stock = serializers.IntegerField()
    image_url = serializers.CharField(max_length=255, allow_blank=True)
    
    def create(self, data):
        return Products.objects.create(data) """
    
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'stock', 'image_url']
    

        
 