from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class SchoolGroup(TimeStampedModel):
    group_number = models.PositiveIntegerField(null=True, blank=True, verbose_name='Numero del grupo')
    school_year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Año del grupo')
    status = models.BooleanField(default=True)