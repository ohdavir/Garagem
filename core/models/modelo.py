from django.db import models

class Modelo(models.model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.id} {self.nome.upper()} {self.marca}"