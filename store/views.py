from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .viewset_base import ViewSetBase


# # Category View
class CategoryListView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateView(generics.UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer




# Product View
class ProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer



# ProductOrder View
class ProductOrderListView(generics.ListAPIView):
    queryset = ProductOrderModel.objects.all()
    serializer_class = ProductOrderSerializer


class ProductOrderCreateView(generics.CreateAPIView):
    queryset = ProductOrderModel.objects.all()
    serializer_class = ProductOrderSerializer


class ProductOrderUpdateView(generics.UpdateAPIView):
    queryset = ProductOrderModel.objects.all()
    serializer_class = ProductOrderSerializer

class ProductOrderDeleteView(generics.DestroyAPIView):
    queryset = ProductOrderModel.objects.all()
    serializer_class = ProductOrderSerializer



# Order View
class OrderListView(generics.ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateView(generics.UpdateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

class OrderDeleteView(generics.DestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer








































# class ProductAPI(ViewSetBase):
#     @staticmethod
#     def get_all_products(request):
#         products = ProductModel.objects.all()
#         return Response(ProductSerializer(products, many=True, read_only=True).data)