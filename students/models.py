from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from professional_careers.models import ProfessionalCareer
from school_groups.models import SchoolGroup
from school_subjects.models import SchoolSubject

# Create your models here.
# Estudiantes
class Student(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='student_user', on_delete=models.CASCADE)
    career = models.ForeignKey(ProfessionalCareer, related_name='student_carrer', blank=True, null=True, on_delete=models.CASCADE)
    school_group = models.ForeignKey(SchoolGroup, related_name='student_school_group', blank=True, null=True, on_delete=models.CASCADE)
    semester = models.PositiveIntegerField(null=True, blank=True, verbose_name='Semestre al cual pertenece el alumno')
    school_subjects = models.ManyToManyField(SchoolSubject, blank=True, related_name='student_school_subjects')

    def __str__(self):
        return 'Estudiante: %s - %s - %s' % (self.user, self.semester, self.career.name)