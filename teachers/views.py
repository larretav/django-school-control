from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer
# Create your views here.

class TeacherViewset(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.filter()
    
    def perform_destroy(self, instance):
        #instance.status = False
        instance.save()