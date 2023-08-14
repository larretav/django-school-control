from rest_framework import serializers
from .models import ProfessionalCareer
from school_subjects.serializers import SchoolSubjectCarrersSerializer

class ProfessionalCareerSerializer(serializers.ModelSerializer):
    school_subjects = SchoolSubjectCarrersSerializer(many=True, source='school_subject_carrer')
    class Meta:
        model = ProfessionalCareer
        fields = '__all__'