from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import File
from .serializers import FileSerializer
from . import serializers
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_list_or_404, get_object_or_404


class FileUploadView(generics.ListCreateAPIView):
    queryset = File.objects.order_by('-id')[:6]
    serializer_class = serializers.FileSerializer

class FileDetailView(generics.RetrieveUpdateAPIView):
    queryset = File.objects.all()
    serializer_class = serializers.FileSerializer

class FileDetailView1(generics.RetrieveUpdateAPIView):
    queryset = File.objects.all()
    serializer_class = serializers.FileSerializer
    


    
# class FileUploadView(APIView):
#     parser_class = (FileUploadParser,)
#     # queryset = File.objects.all()
#     # serializer_class = FileSerializer
#     # # print('^^^^^^^^^~~~~~~~', queryset)
#     # def get(self, request, *args, **kwargs):
#     #     print("here ==>")
#     #     users = File.objects.all()
#     #     serializer =FileSerializer(users, many=True)
#     #     print("==>", serializer.data)
#     #     return Response(serializer.data)

#     def post(self, request, *args, **kwargs):

#       file_serializer = FileSerializer(data=request.data)

#       if file_serializer.is_valid():
#           file_serializer.save()
#           return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#       else:
#           return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


