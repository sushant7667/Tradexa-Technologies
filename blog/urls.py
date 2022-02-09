from django.urls import path, include
from .views import *

urlpatterns = [
    path('blog/', login, name='login')
]
