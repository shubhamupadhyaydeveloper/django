from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializer import ProductSerializer



# Create your views here.
def product_home(request):
    products = Product.objects.all()
    return render(request,'products/product.html',{'products' : products})

@api_view(['GET'])
def product_detail(request,product_id:int):
    product_details = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product_details)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)