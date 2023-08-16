from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ProfessionalCareer
from .serializers import ProfessionalCareerSerializer
# Create your views here.

class ProfessionalCareerViewset(viewsets.ModelViewSet):
    serializer_class = ProfessionalCareerSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return ProfessionalCareer.objects.filter(status=True)
    
    def perform_destroy(self, instance):
        instance.status = False
        instance.save()
