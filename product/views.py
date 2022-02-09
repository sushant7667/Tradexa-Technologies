from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import productModel
from .serializers import productSerializer


# Due to lack of time because of exams I was not able to include higher order authentication and authorization
# the request can be manipulated based upon the authorization
# Generally I use APIView because it quite good for server side data manipulation
class productAPI(APIView):
    @staticmethod
    def get():
        model = productModel.objects.all()
        serializer = productSerializer(model, many=True)
        return Response(serializer.data, status=200)

    @staticmethod
    def post(request):
        serializer = productSerializer(data=request.data, many=True, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Saved"}, status=200)
        return Response({"Response": "Bad Request"}, status=400)