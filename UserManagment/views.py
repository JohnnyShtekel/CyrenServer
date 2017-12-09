from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from UserManagment.models import *
from UserManagment.serializers.user_serializer import UserSerializer
import pdb;


@csrf_exempt
def update_user_data(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = User.objects.get(pk=data['id'])
        user.status = data['status']
        user.save()
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




@csrf_exempt
def user_by_user_name(request,userName):
    if request.method == 'GET':
        try:
            user = User.objects.get(userName=userName)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False)
        except User.DoesNotExist:
            return HttpResponse(status=404)

@csrf_exempt
def user_by_status_and_id(request,status,id):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=id,status=status)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False)
        except User.DoesNotExist:
            return HttpResponse(status=404)


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        users = User.objects.exclude(pk=data)
        serializer = UserSerializer(users,many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)