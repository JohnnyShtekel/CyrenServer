from rest_framework import serializers
from UserManagment.models import *


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    userName = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.id = validated_data.get('id', instance.id)
        instance.userName= validated_data.get('userName', instance.userName)
        instance.status = validated_data.get('status', instance.status)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.save()
        return instance