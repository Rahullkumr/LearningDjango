from django.shortcuts import render, HttpResponse
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def students(request):
    if request.method == 'GET':
        model_instance = StudentModel.objects.all()
        ser_data = StudentSerializer(model_instance, many=True)
        py_data = ser_data.data
        json_data = JSONRenderer().render(py_data)
        return HttpResponse(json_data)

    if request.method == 'POST':
        req_data = request.body
        stream_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        de_ser = StudentSerializer(data=py_data)
        if de_ser.is_valid():
            de_ser.save()
            msg = {'msg': 'data submitted successfully'}
            return HttpResponse(JSONRenderer().render(msg))


@csrf_exempt
def student(request, pk):
    try:
        stu = StudentModel.objects.get(id=pk)
    except:
        msg = {'msg': 'No data found'}
        return HttpResponse(JSONRenderer().render(msg))

    if request.method == 'PUT':
        req_data = request.body
        stream_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        de_ser = StudentSerializer(stu, data=py_data)
        if de_ser.is_valid():
            de_ser.save()
            msg = {'msg': 'Data submitted successfully'}
            return HttpResponse(JSONRenderer().render(msg))

    if request.method == 'PATCH':
        req_data = request.body
        stream_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        # partial=True for PATCH
        de_ser = StudentSerializer(stu, data=py_data, partial=True)
        if de_ser.is_valid():
            de_ser.save()
            msg = {'msg': 'Data partially updated successfully'}
            return HttpResponse(JSONRenderer().render(msg))

    if request.method == 'DELETE':
        stu.delete()
        msg = {'msg': 'Data deleted successfully'}
        return HttpResponse(JSONRenderer().render(msg))
