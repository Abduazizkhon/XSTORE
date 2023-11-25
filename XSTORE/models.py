from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import *



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    is_customer = models.BooleanField(default=True) #if 0 it is a staff, if 1 it is a customer
    photo = models.ImageField(null = True, blank = True, upload_to="users")
    birthday = models.DateField(null=True)
    balance = models.FloatField(default=0) #balance for staff is salary, for client it is amount in wallet
    position  = models.ForeignKey("Position", null=True, on_delete=models.SET_NULL)
    departament = models.ForeignKey("Departament", null=True, on_delete=models.SET_NULL, related_name="rel2") 
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 
    objects = Manager()

class Departament(models.Model):
    name = models.CharField(max_length=20)
    head = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="rel1")

class Position(models.Model):
    name = models.CharField(max_length=40)


# class Staff(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) #connected staff to the user
#     position  = models.ForeignKey()
#     departament = models.ForeignKey(Departament, null=True, on_delete=models.SET_NULL) #CASCADE means if u delete this value of the attribute whole obj will be  deleted

class Category(models.Model):
    name = models.CharField(max_length=20)

class Producer(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    price = models.FloatField()
    expiration_date = models.DateField()
    quantity = models.IntegerField()
    description  = models.TextField()
    photo = models.ImageField(null = True, blank = True, upload_to="products")
    producer = models.ForeignKey("Producer", null=True, on_delete=models.SET_NULL)
    is_popular = models.BooleanField(default=False)


    







    





