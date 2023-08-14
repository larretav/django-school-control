from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
#Carreras
class ProfessionalCareer(TimeStampedModel):
    program_number = models.PositiveIntegerField(null=True, blank=True,verbose_name='Numero del programa')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre de la carrera')
    number_semesters = models.PositiveIntegerField(null=True, blank=True,verbose_name='Numero de semestres')
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.number_semesters)