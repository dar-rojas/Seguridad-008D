from django.db import models
from django.contrib.auth.models import User

class Reclamo(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    asunto = models.CharField(max_length=150)
    cuerpo = models.TextField(max_length=1000)
    estado = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Reclamo #{self.id} - {self.asunto}'