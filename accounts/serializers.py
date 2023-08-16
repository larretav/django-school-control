from rest_framework import serializers
from django.contrib.auth.models import Group

from .models import User
from students.models import Student
from teachers.models import Teacher
from professional_careers.models import ProfessionalCareer
from school_groups.models import SchoolGroup
from school_subjects.models import SchoolSubject

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

class UserAccountStudentRegisterSerializer(serializers.Serializer):
    userKey = serializers.CharField()
    password = serializers.CharField(write_only=True)
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    email = serializers.EmailField()
    birthdate = serializers.DateField()
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES)
    photoUrl = serializers.CharField()
    professionalCareer = serializers.PrimaryKeyRelatedField(queryset=ProfessionalCareer.objects.all())


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['userKey'],
            email=validated_data['email'],
            first_name=validated_data['firstName'],
            last_name=validated_data['lastName'],
            gender=validated_data['gender'],
            birthday=validated_data['birthdate'],
            photo_url=validated_data['photoUrl'],
        )
        user.set_password(validated_data['password'])
        user.save()

        student = Student.objects.create(
            user=user,
            career=validated_data['professionalCareer']
        )

        return user, student
    
class UserAccountTeacherRegisterSerializer(serializers.Serializer):
    userKey = serializers.CharField()
    password = serializers.CharField(write_only=True)
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    email = serializers.EmailField()
    birthdate = serializers.DateField()
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES)
    photoUrl = serializers.CharField()
    schoolGroups = serializers.PrimaryKeyRelatedField(queryset=SchoolGroup.objects.all(), many=True)
    schoolSubjects = serializers.PrimaryKeyRelatedField(queryset=SchoolSubject.objects.all(), many=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['userKey'],
            email=validated_data['email'],
            first_name=validated_data['firstName'],
            last_name=validated_data['lastName'],
            gender=validated_data['gender'],
            birthday=validated_data['birthdate'],
            photo_url=validated_data['photoUrl'],
        )
        user.set_password(validated_data['password'])
        user.save()
        teacher = Teacher.objects.create(
            user=user
        )
        teacher.school_groups.set(validated_data.pop('schoolGroups'))
        teacher.school_subjects.set(validated_data.pop('schoolSubjects'))

        return user, teacher