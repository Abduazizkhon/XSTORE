from this import d
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import *
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ProductsAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        manual_parameters = [
            openapi.Parameter(name = "search", in_ = openapi.IN_QUERY, type = openapi.TYPE_STRING, required = False)],
        responses = {200: ProductSerializer()})
    def get(self, request):
        goods = Product.objects.all()
        if "search" in request.GET.keys():
            search = request.GET["search"]
            goods = goods.filter(name__contains = search)
        data = ProductSerializer(goods, many = True).data
        return Response(data, status = status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body = ProductSerializer(), 
        responses = {
            200: ProductSerializer(),
            400: "Serializer's Errors"
        }
    )
    def post(self, request):
       
        serializer = ProductSerializer(data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            goods = Product.objects.all()
            data = ProductSerializer(goods, many = True).data
            return Response(data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
    request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT, 
            required = ["id"],
            properties = {
                "id": openapi.Schema(type = openapi.TYPE_INTEGER),
                "name": openapi.Schema(type = openapi.TYPE_STRING),
                "category": openapi.Schema(type = openapi.TYPE_INTEGER),
                "price": openapi.Schema(type = openapi.TYPE_NUMBER),
            }
        ),
        responses = {200: ProductSerializer(), 400: "Error"})
    def patch(self, request):
        id = request.data["id"]
        product = Product.objects.get(id = id)
        serializer = ProductSerializer(product, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # if u give to the serializer data and instance u upodate it, 
    # if u give only the instance means u wanna convert to the JSON
    # if u give data then u wanna create new object




# Homework  
    def popular(self, request):
        goods = Product.objects.filter(is_popular = True)
        data = ProductSerializer(goods, many = True).data
        return Response(data, status = status.HTTP_200_OK)

        

class SelfAPIView(APIView):
    permission_class = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses = {200: SelfSerializer()})
    def get(self, request):
        info = request.user
        data = SelfSerializer(info).data
        return Response(data, status = status.HTTP_200_OK)

# Homework

class CategoriesAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses = {200: CategorySerializer()})
    def get(self, request):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many = True).data
        return Response(data, status = status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body = CategorySerializer(), 
        responses = {
            200: CategorySerializer(),
            400: "Serializer's Errors"
        }
    )

    def post(self, request):
       
        serializer = CategorySerializer(data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            categories = Category.objects.all()
            data = CategorySerializer(categories, many = True).data
            return Response(data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT, 
            required = ["id"],
            properties = {
                "id": openapi.Schema(type = openapi.TYPE_INTEGER)
            }
        ),
        responses = {200: "Caegory is deleted"})
    def delete(self, request):
        id = request.data["id"]
        category = Category.objects.get(id = id)
        category.delete()
        return Response({"Message": "Caegory is deleted"}, status = status.HTTP_200_OK)
    

    @swagger_auto_schema(
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT, 
            required = ["id", "name"],
            properties = {
                "id": openapi.Schema(type = openapi.TYPE_INTEGER),
                "name": openapi.Schema(type = openapi.TYPE_STRING)
            }
        ),
        responses = {200: CategorySerializer(), 400: "Error"})
    def patch(self, request):
        id = request.data["id"]
        category = Category.objects.get(id = id)
        serializer = CategorySerializer(category, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)






    



