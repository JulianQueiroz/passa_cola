from django.db import models

# Create your models here.
class Avaliacao(models.Model):
    materia = models.CharField(max_length=100)
    avaliacao = models.CharField(max_length=3000)

    def __str__(self):
        return f"{self.materia},{self.avaliacao}"