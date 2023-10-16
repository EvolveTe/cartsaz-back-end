from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# router = DefaultRouter()
# router.register('category', CategoryView)

urlpatterns = [
    # path('', include(router.urls)),
    # path('product/', ProductAPI.as_view({"get": "get_all_products"})),
    path('categoryList/', CategoryListView.as_view()),
    path('categoryCreate/', CategoryCreateView.as_view()),
    path('categoryUpdate/<int:pk>', CategoryUpdateView.as_view()),
    path('categoryDelete/<int:pk>', CategoryDeleteView.as_view()),
    path('productList/', ProductListView.as_view()),
    path('productCreate/', ProductCreateView.as_view()),
    path('productUpdate/', ProductUpdateView.as_view()),
    path('productDelete/', ProductDeleteView.as_view()),
    path('productOrderList/', ProductOrderListView.as_view()),
    path('productOrderCreate/', ProductOrderCreateView.as_view()),
    path('productOrderUpdate/', ProductOrderUpdateView.as_view()),
    path('productOrderDelete/', ProductOrderDeleteView.as_view()),
    path('OrderList/', OrderListView.as_view()),
    path('OrderCreate/', OrderCreateView.as_view()),
    path('OrderUpdate/', OrderUpdateView.as_view()),
    path('OrderDelete/', OrderDeleteView.as_view()),
]
