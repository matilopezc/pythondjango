from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=45,default='')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=45,default='')
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre