from rest_framework import serializers
from .models import productModel


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = productModel
        fields = "__all__"
