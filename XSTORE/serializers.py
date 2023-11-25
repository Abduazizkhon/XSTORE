from rest_framework.serializers import ModelSerializer
from .models import *

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SelfSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    
    