from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True) #null = True para imágenes
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True) #unique = no se repita
    anulate = models.BooleanField('Anulado', default=False) #anulado = como se visualiza en el admin
    #editable = para que sea posible modificar este valor

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name'] #['-name'] al reves
        unique_together = ('name','short_name') #no se pueden repetir name y short_name

    def __str__(self): #nombre en la bd
        return str(self.id) + '-' + self.name + '-' + self.short_name