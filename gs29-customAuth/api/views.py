from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from api.customauth import CustomAuthentication
  ### ModelViewSet Class API CRUD ###
 
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # Global Auth Can be overrided..

    #Basic Authentication
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAdminUser]

    #Session Authentication
  
    authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[AllowAny]
    #permission_classes=[IsAdminUser]
    #permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissions]





      

   ### ViewSet Router API ###

# class StudentViewSet(viewsets.ViewSet):
#     def list(self,request):
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         id=pk
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
        
    
#     def create(self,request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated '})
#         return Response(serializer.errors)

#     def update(self,request,pk):
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated '})
#         return Response(serializer.errors)
    
#     def partial_update(self,request,pk):
#         id=pk  
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated '})
#         return Response(serializer.errors)
    
#     def destroy(self,request,pk):
#         id=pk
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})
    
    
    
    

    




          ### Concrete Based APIView CRUD ###
#PK Not Required
# class StudentListCreate(ListCreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# #PK Required
# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


  

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




