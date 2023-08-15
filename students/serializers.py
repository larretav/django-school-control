from rest_framework import serializers
from .models import Student
from accounts.serializers import UserStudentSerializer
from professional_careers.serializers import ProfessionalCareerStudentSerializer
from school_subjects.serializers import SchoolSubjectStudentSerializer

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ('created', 'modified')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserStudentSerializer(instance.user).data
        response['career'] = ProfessionalCareerStudentSerializer(instance.career).data
        response['school_group'] = str(instance.school_group)
        response['school_subjects'] = SchoolSubjectStudentSerializer(instance.school_subjects, many=True).data
        return response