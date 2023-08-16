from rest_framework import serializers
from .models import Teacher
from accounts.serializers import UserStudentSerializer
from school_subjects.serializers import SchoolSubjectStudentSerializer
from school_groups.serializers import SchoolGroupSerializer

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        exclude = ('created', 'modified')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserStudentSerializer(instance.user).data
        response['school_groups'] = SchoolGroupSerializer(instance.school_groups, many=True).data
        response['school_subjects'] = SchoolSubjectStudentSerializer(instance.school_subjects, many=True).data
        return response