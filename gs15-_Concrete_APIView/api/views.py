from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView



          ### Concrete Based APIView CRUD ###
# Get All Data
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Post Data
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Get Data By ID
class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Update Data By ID
class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Delete Data By ID
class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Get All Data and Post New Data
class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Get and Update Data By ID
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Get And Delete Data By ID
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#  Get , Update And Delete Data by ID
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer





















      #######  Generic Mixin Based APIView CRUD  #####
     # List and Create - PK Not Required 

# class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# # Retrive Update and Destroy - PK Required 
# class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
    
    
    
        

 

          



      #######  CLASS Based APIView CRUD  ##########
      
# class StudentAPI(APIView):
#     def get(self,request,pk=None,format=None):
#         if request.method=='GET':
#             id=pk
#             if id is not None:
#                 stu=Student.objects.get(id=id)
#                 serializer=StudentSerializer(stu)
#                 return Response(serializer.data)
#             stu=Student.objects.all()
#             serializer=StudentSerializer(stu,many=True)
#             return Response(serializer.data)
    
#     def post(self,request,pk=None,format=None):
#         if request.method=='POST':
#             serializer=StudentSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Data Created '})
#             return Response(serializer.errors)
        
#     def put(self,request,pk=None,format=None):
         
#         if request.method=='PUT':
#             id=pk 
#             stu=Student.objects.get(pk=id)
#             serializer=StudentSerializer(stu,data=request.data,partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':' complete Data Updated '})
#             return Response(serializer.errors)
        
#     def patch(self,request,pk=None,format=None):
         
#         if request.method=='PATCH':
#             id=pk 
#             stu=Student.objects.get(pk=id)
#             serializer=StudentSerializer(stu,data=request.data,partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':' complete Data Updated '})
#             return Response(serializer.errors)
    
#     def delete(self,request,pk=None,format=None):
#         if request.method=='DELETE':
#             id=pk 
#             stu=Student.objects.get(pk=id)
#             stu.delete()
#             return Response({'msg':'Data Deleted !!! '})

        
        
    
    


        
        
#######  Function Based APIView CRUD  #################

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_api(request,pk=None):
#     if request.method=='GET':
#         id=pk 
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    

#     if request.method=='POST':
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created '})
#         return Response(serializer.errors)
    
#     if request.method=='PUT':
#         id=pk 
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':' complete Data Updated '})
#         return Response(serializer.errors)
    
#     if request.method=='PATCH':
#         id=pk 
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'partial Data Updated '})
#         return Response(serializer.errors)
    

#     if request.method=='DELETE':
#         id=pk 
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted !!! '})




