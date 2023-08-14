from django.db import models
from django_extensions.db.models import TimeStampedModel
from professional_careers.models import ProfessionalCareer

# Create your models here.
# materias
class SchoolSubject(TimeStampedModel):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre de la materia')
    semester = models.PositiveIntegerField(null=True, blank=True, verbose_name='Semestre al cual pertenece la materia')
    career = models.ForeignKey(ProfessionalCareer, related_name='school_subject_carrer', blank=True, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.semester, self.career.name)
