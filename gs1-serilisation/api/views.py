from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.
def student_detail(request,pk):
    stu=Student.objects.get(id=pk )  # complex datatype
    print(stu)
    serializer=StudentSerializer(stu)  # Python Native datatype
    print(serializer)
    json_data=JSONRenderer().render(serializer.data) # Json Data format
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data)
 

#Query Set - All Student Data
def student_list(request):
    stu=Student.objects.all()                   # Complex datatype
    
    serializer=StudentSerializer(stu,many=True) # Python Native datatype
    
    json_data=JSONRenderer().render(serializer.data)  # Json data format
    
    return HttpResponse(json_data,content_type='application/json')
   #return JsonResponse(serializer.data,safe=False)


