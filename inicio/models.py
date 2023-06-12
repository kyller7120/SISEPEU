from django.db import models

# Create your models here.
class Matricula(models.Model):
    anio = models.IntegerField('Año')
    universidad = models.CharField('Universidad', max_length=200)
    facultad = models.CharField('Facultad', max_length=200)
    carrera = models.CharField('Carrera', max_length=200)
    cantidad = models.IntegerField('Cantidad')

    def __str__(self):
        return str(self.anio) + '|' + self.universidad + '|' + self.facultad + '|' + self.carrera + '|' + str(self.cantidad)

class Egreso(models.Model):
    anio = models.IntegerField('Año')
    universidad = models.CharField('Universidad', max_length=200)
    facultad = models.CharField('Facultad', max_length=200)
    carrera = models.CharField('Carrera', max_length=200)
    cantidad = models.IntegerField('Cantidad')
    
    def __str__(self):
        return str(self.anio) + '|' + self.universidad + '|' + self.facultad + '|' + self.carrera + '|' + str(self.cantidad)