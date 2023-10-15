from django.db import models
from core.models import BaseModel
from user.models import BaseUser
from rest_framework.serializers import ModelSerializer



class CategoryModel(BaseModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

class ProductModel(BaseModel):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    code = models.IntegerField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description = models.TextField()
    showcase = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    

    def __str__(self):
        return self.name
    

class ProductOrderModel(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)


class OrderModel(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductOrderModel)
    status = models.CharField(max_length=100, default='pending')




class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'




class ProductOrderSerializer(ModelSerializer):
    class Meta:
        model = ProductOrderModel
        exclude = ('user')


class OrderSerializer(ModelSerializer):
    products = ProductOrderSerializer(many=True, read_only=True)

    class Meta:
        model = OrderModel
        fields = '__all__'