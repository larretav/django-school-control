from rest_framework import viewsets
from .models import ProfessionalCareer
from .serializers import ProfessionalCareerSerializer
# Create your views here.

class ProfessionalCareerViewset(viewsets.ModelViewSet):
    serializer_class = ProfessionalCareerSerializer

    def get_queryset(self):
        return ProfessionalCareer.objects.filter(status=True)
    
    def perform_destroy(self, instance):
        instance.status = False
        instance.save()
