from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=('Kullanıcı'), on_delete=models.CASCADE)
    name = models.CharField(('Kullanıcı'),max_length=50)
    image =models.ImageField(('Profil Resmi'),upload_to='profil', max_length=100)
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.title
    
    
class Blog(models.Model):
    category = models.ForeignKey(Category,verbose_name="Kategori",on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"), max_length=500)
    date_now = models.DateTimeField(("Tarih"),auto_now_add=True)
    image = models.FileField(("Resim"),upload_to="")
    
    def __str__(self):
        return self.title
