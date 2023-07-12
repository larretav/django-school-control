from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class SchoolSubject(TimeStampedModel):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre de la materia')
    semester = models.PositiveIntegerField(null=True, blank=True, verbose_name='Semestre al cual pertenece la materia')
    status = models.BooleanField(default=True)