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

class UserStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'email', 'photo_url', 'gender', 'email_validation', 'status')
    
    def get_full_name(self, obj):
        return str(obj)
class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)