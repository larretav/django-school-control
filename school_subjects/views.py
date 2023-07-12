from rest_framework import viewsets
from .models import SchoolSubject
from .serializers import SchoolSubjectSerializer
# Create your views here.

class SchoolSubjectViewset(viewsets.ModelViewSet):
    serializer_class = SchoolSubjectSerializer

    def get_queryset(self):
        return SchoolSubject.objects.filter(status=True)
    
    def perform_destroy(self, instance):
        instance.status = False
        instance.save()