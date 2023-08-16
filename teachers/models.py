from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from school_groups.models import SchoolGroup
from school_subjects.models import SchoolSubject

# Create your models here.
# Maestros
class Teacher(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='teacher_user', on_delete=models.CASCADE)
    school_groups = models.ManyToManyField(SchoolGroup, blank=True, related_name='teacher_school_group')
    school_subjects = models.ManyToManyField(SchoolSubject, blank=True, related_name='teacher_school_subjects')

    def __str__(self):
        return 'Maestro: %s' % (self.user)