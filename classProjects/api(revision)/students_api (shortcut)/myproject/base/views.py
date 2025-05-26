from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import StudentModel
from .serializers import StudentSerializer
import json


@csrf_exempt
def students(request):
    if request.method == 'GET':
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student(request, pk):
    try:
        student = StudentModel.objects.get(id=pk)
    except StudentModel.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student deleted'}, status=204)
