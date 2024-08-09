from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    enail = models.EmailField()
    telafono = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.nombre)
    
    
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def _str_(self):
        return str(self.nombre)
    
        