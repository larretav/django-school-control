from rest_framework import serializers
from .models import ProfessionalCareer

class ProfessionalCareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfessionalCareer
        fields = '__all__'