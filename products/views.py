#Django REST framework
from django.shortcuts import render
from products.models import Products
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt


#serializer
from products.serializers import ProductsSerializer
     
     
@api_view(['GET'])
def get_one(request, productId):
    try:
        product = Products.objects.get(pk=productId)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductsSerializer(product)
    return Response(serializer.data)
    

@api_view(['GET'])
def get_all(request):
    product = Products.objects.all()
    serializer = ProductsSerializer(product, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def create(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    