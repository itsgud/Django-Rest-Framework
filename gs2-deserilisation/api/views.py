from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt 
def student_create(request):
    if request.method=='POST':
        json_data=request.body                  #  Getting Json data
        stream = io.BytesIO(json_data)          #  Parse Json data
        pythondata=JSONParser().parse(stream)    # Python Native Datatype 
        serializer=StudentSerializer(data=pythondata)       # DeSerilisation
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    return HttpResponse('<h1>failed to create </h1>')
        

        


