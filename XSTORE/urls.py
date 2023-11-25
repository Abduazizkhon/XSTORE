import imp
from django.urls import path
from .views import *

urlpatterns = [
    path("products", ProductsAPIView.as_view(), name = "products"),
    path("user", SelfAPIView.as_view(), name = "self"),
    path("category", CategoriesAPIView.as_view(), name = "category")
]