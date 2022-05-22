from operator import index
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', frontpage),
    path('<slug:fcb_class>/home', home),
    
]
