from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno ")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno ")
    nombre=models.CharField(max_length=100,verbose_name="nombre")
    fecha_nacimiento=models.DateField(verbose_name="fecha de nacimiento",null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name="fecha de ingreso",null=False,blank=False)