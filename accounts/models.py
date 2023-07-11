from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django_extensions.db.models import TimeStampedModel

def upload_photo_file(instance, filename):
    x = filename.split('.')
    if(x.pop() not in ('jpg','jpeg','png')):
        raise ValidationError('Extension de archivo invalida.')
    return f'photo_user/{instance.id}/{filename}'

class User(AbstractUser, PermissionsMixin, TimeStampedModel):
    GENDER_CHOICES = [
        ('M', 'Hombre'),
        ('F', 'Mujer'),
        ('X', 'No binario'),
    ]

    email_validation = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='X')
    birthday = models.DateField(verbose_name='Fecha de nacimiento', null=True)
    photo_url = models.FileField(upload_to=upload_photo_file, verbose_name="Foto del usuario", blank=True, null=True)
    status = models.BooleanField(default=True)

