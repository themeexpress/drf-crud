from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class ProductServices:
    """ Retrive all products """
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_product_by_id(pk):
        return get_object_or_404(Product, pk=pk)
    
    @staticmethod
    def create_product(data):
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer
    
    @staticmethod
    def update_product(pk, data):
        """" Update existing product"""
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer
    
    @staticmethod
    def delete_product(pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return {"message": "Product deleted successfully!!"}


    
