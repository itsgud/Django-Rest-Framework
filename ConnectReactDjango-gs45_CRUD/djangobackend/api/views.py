from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import  ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
# Create your views here.

class StudentList(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer 
 

#PK Required
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
