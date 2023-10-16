from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from rest_framework.serializers import ModelSerializer
# from apps.Idea.models import IdeaModel

class BaseUserManager(BUM):
    def create_user(self, full_name, store_instagram_id, store_name, phone_number, store_type, email, address, postal_code, is_active=True, is_admin=False, password=None, *args, **kwargs):

        if not phone_number:
            raise ValueError("Users must have an uniqe phone_number")

        user = self.model(
            full_name=full_name,
            store_name=store_name,
            phone_number=phone_number,
            store_instagram_id=store_instagram_id,
            store_type=store_type,
            email=email,
            address=address,
            postal_code=postal_code,
            is_active=is_active,
            is_admin=is_admin,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, store_instagram_id, store_name, phone_number, store_type, email, address, postal_code, password=None, *args, **kwargs):
        user = self.create_user(
            full_name=full_name,
            store_name=store_name,
            phone_number=phone_number,
            store_instagram_id=store_instagram_id,
            store_type=store_type,
            email=email,
            address=address,
            postal_code=postal_code,
            is_active=True,
            is_real_estate=False,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user



class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    
    full_name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField(unique=True)
    store_instagram_id = models.CharField(max_length=100)
    store_type = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = "store_name"

    REQUIRED_FIELDS = ['full_name', 'store_instagram_id', "phone_number",  'store_type', 'email', 'address', 'postal_code']

    def __str__(self):
        return f"{self.store_name} , {self.full_name}"

    def is_staff(self):
        return self.is_admin






#serializers
class BaseUserSerializer(ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ['id', 'full_name', 'store_instagram_id', 'store_name', 'store_type', 'email', 'address', 'postal_code', "phone_number"]








# class SocialNetworksModel(BaseModel):
#     Website = models.URLField(max_length=500)
#     Email = models.EmailField(max_length=150)
#     Eitaa = models.CharField(max_length=150)
#     Bale = models.CharField(max_length=150)
#     Rubika = models.CharField(max_length=150)
#     Soroush = models.CharField(max_length=150)
    
    
    
    
# class SocialNetworksSerializer(ModelSerializer):
#     class Meta:
#         model = SocialNetworksModel
#         fields = ['Website', 'Email', 'Eitaa', 'Bale', 'Rubika', 'Soroush']
        
        
        
        
        
        
        
        
        
        
# class AuthenticationModel(BaseModel):
#     Email = models.EmailField(max_length=254)
#     Phone = models.IntegerField()
    

          