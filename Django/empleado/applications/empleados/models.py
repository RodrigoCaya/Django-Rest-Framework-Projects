from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
    
    def __str__(self): #nombre en la bd
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #avatar = models.ImageField(upload_to='empleado', null=True, blank=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi persona'
        verbose_name_plural = 'Personas de la empresa'
        ordering = ['first_name'] #['-name'] al reves
        unique_together = ('first_name','last_name','job')

    def __str__(self): #nombre en la bd
        return str(self.id) + '-' + self.first_name + '-' + self.last_name