from django.shortcuts import render
from rest_framework import viewsets
from .models import *


class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer