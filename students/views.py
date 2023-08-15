from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter()
    
    def perform_destroy(self, instance):
        #instance.status = False
        instance.save()