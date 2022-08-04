from unicodedata import name
from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado

# Create your views here.

# 1.- Listar de todos los empleados de la empresa
# 2.- Listar de todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado

#1
class ListAllEmpleados(ListView):
    template_name = 'empleados/lista.html'
    model = Empleado

#2
class ListByAreaEmpleados(ListView):
    template_name = 'empleados/lista_by_area.html'
    #queryset = Empleado.objects.filter(
    #    departamento__name = 'Ladron'
    #)
    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        area = self.kwargs['name_url']
        lista = Empleado.objects.filter(
            departamento__name = area
        )
        return lista

#3
class ListByJobEmpleados(ListView):
    template_name = 'empleados/lista_by_job.html'
    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        area = self.kwargs['name_url']
        lista = Empleado.objects.filter(
            job = area # 0,1,2,3
        )
        return lista

#4
class ListByKeyWordEmpleados(ListView):
    template_name = 'empleados/lista_by_kw.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista