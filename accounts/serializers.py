from rest_framework import serializers
from django.contrib.auth.models import Group


from .models import User

class UserSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'groups', 'is_active', 'is_superuser')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['groups'] = GroupsSerializer(instance.groups, many=True).data #regresa los grupos serializados
            
        return response

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)