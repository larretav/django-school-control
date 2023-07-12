from rest_framework import viewsets
from .models import SchoolGroup
from .serializers import SchoolGroupSerializer
# Create your views here.

class SchoolGroupViewset(viewsets.ModelViewSet):
    serializer_class = SchoolGroupSerializer

    def get_queryset(self):
        return SchoolGroup.objects.filter(status=True)
    
    def perform_destroy(self, instance):
        instance.status = False
        instance.save()