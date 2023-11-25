from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([User, 
                     Departament, 
                     Category,
                     Product,
                     Position,
                     Producer
                     ])