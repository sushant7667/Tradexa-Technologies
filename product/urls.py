from django.urls import path, include
from .views import *

urlpatterns = [
    path('', productAPI.as_view(), name='login')
]
