from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student 
from django.views.decorators.csrf import csrf_exempt
     
@csrf_exempt   
def student_api(request):
    #GET--- it shows data through id..
    if request.method=='GET':
        json_data=request.body 
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        print("id is getting from extrnl---  ",id)
        if id is not None:
            print("innnn the idd ")
            stu=Student.objects.get(id=id) 
            print(stu)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        stu = Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
       #POST-- it add the data
     
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    #PUT------  update data

    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        print("idd is-- ",id)
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updatedd'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    # Delete--- to delete data from DB

    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted!!! '}
        json_data= JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        
    # json_data=JSONRenderer().render(serializer.errors)
    # return HttpResponse(json_data,content_type='application/json')
    


        
            
        

        



        
        
        # if serializer.is_valid():
        #     serializer.save()
        #     res={'msg':'Data created'}
        #     json_data= JSONRenderer().render(res)
        #     return HttpResponse(json_data,content_type='application/json')
        
        # json_data=JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data,content_type='application/json')
        

        


