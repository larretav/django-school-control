from rest_framework import serializers
from .models import SchoolSubject
from professional_careers.models import ProfessionalCareer

class SchoolSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolSubject
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['career'] = ProfessionalCareerSchoolSubjectSerializer(instance.career).data #Regresa los tipos de evidencia serializadas
        return response

class SchoolSubjectCarrersSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolSubject
        exclude = ('career',)

class ProfessionalCareerSchoolSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalCareer
        fields = '__all__'