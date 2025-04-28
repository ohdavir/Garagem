from django.db import models

class Acessorio(models.Model):
    discricao = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.discricao    
        return self.id