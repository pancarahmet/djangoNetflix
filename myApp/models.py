from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=('Kullanıcı'),on_delete=models.CASCADE)
    password = models.CharField(('Password'),max_length=50)
    phone_number = PhoneField(blank=True, help_text='Telefon Numarası')
    
    def __str__(self):
        return self.user.username
    



