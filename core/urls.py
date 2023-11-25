"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view #drf-yasg has view that creates documentation
from drf_yasg import openapi # 
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = "XSTORE",
        default_version = "1.0",
        description = "Grocery Store in Tashkent",
        terms_of_service = "",
        contact = openapi.Contact(name = "abdu", email = "abduazizkhon.09@gmail.com", url = "https://github.com/Abduazizkhon"),
        license = openapi.License(name = "", url = ""),
    ),
    patterns = [
        path("", include("XSTORE.urls")),

    ],
    public = True, 
    permission_classes = [permissions.AllowAny]
    
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("XSTORE.urls")),
    path("swagger", schema_view.with_ui())
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
