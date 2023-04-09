from django.db import models

# Create your models here.


class Movies(models.Model):
    name=models.CharField(max_length=50)
    resim=models.FileField(upload_to="afis",verbose_name="Afis Resmi",blank=True,null=True)

    def __str__(self):
        return self.name
