from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    #queryset=Student.objects.filter(passby='user1')
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    #search_fields=['city']
    search_fields=['^name']
     