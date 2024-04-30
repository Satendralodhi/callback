from django.shortcuts import render
from rest_framework.views import APIView
from .serailizers import callback_serializers
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

class call_backApi(APIView):
    def post(self,request,*args, **kwargs):
        print(request.data)
        serializer=callback_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data})
        else:
            return Response({'errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
# Create your views here.
