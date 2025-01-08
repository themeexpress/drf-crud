from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import ProductServices
from .serializers import ProductSerializer

class ProductListView(APIView):
    """ handle GET and POST for products"""
    def get(self, request):
        products = ProductServices.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductServices.create_product(request.data)
        return Response(serializer.data, status.HTTP_201_CREATED)

class ProductDetailView(APIView):
    """handle GET, PUT, and DELETE for single product"""
    def get(self, request, pk):
        product = ProductServices.get_product_by_id(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        serializer = ProductServices.update_product(pk, request.data)
        return Response(serializer.data)
    
    def delete(self, request, pk):
       ProductServices.update_product(pk, request.data)
       return Response({"message": "Product deleted successfully!!"})
