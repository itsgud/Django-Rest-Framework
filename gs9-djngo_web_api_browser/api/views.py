from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()   #by defalut GET method is iniliased
# def helloworld(request):
#     return Response({'msg':'Helllo world'})

# @api_view(['POST'])
# def helloworld(request):
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg':' this is  POst Request'})
     
@api_view(['GET','POST'])
def helloworld(request):
    if request.method=='GET':
        return Response({'msg':'This is Get Request'})
    if request.method=='POST':
        print(request.data)
        return Response({'msg':' this is  POst Request','data':request.data})
    
    
   


