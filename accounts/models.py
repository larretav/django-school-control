from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, UserManager
from django_extensions.db.models import TimeStampedModel

def upload_photo_file(instance, filename):
    x = filename.split('.')
    if(x.pop() not in ('jpg','jpeg','png')):
        raise ValidationError('Extension de archivo invalida.')
    return f'photo_user/{instance.id}/{filename}'
#NOTA: ACTUALMENTE HAY UN PROBLEMA CON LA CONTRASEÑA QUE NO SE ESTA
#CODIFICANDO
class User(AbstractUser, TimeStampedModel):
    GENDER_CHOICES = [
        ('M', 'Hombre'),
        ('F', 'Mujer'),
        ('X', 'No binario'),
    ]

    email_validation = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='X')
    birthday = models.DateField(verbose_name='Fecha de nacimiento', null=True)
    photo_url = models.CharField(max_length=500, verbose_name="Foto del usuario", blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)