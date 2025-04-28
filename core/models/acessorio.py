from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.id} {self.descricao}"