import json
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from .models import Person, Reunion
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    PersonaSerializer3,
    ReunionSerializer,
    ReunionSerializer2,
    ReunionSerializerLink,
)

#manera normal
class ListaPersonas(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

#manera con rest_framework
class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = 'persona/lista.html'

class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        #filtrar datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains = kword
        )

#### CRUD
class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer

class PersonRetrieveView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateView(UpdateAPIView): #no muestra ningun valor
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonRetrieveUpdateView(RetrieveUpdateAPIView): #muestra todos los valores
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

#### distinto serializer
class PersonAPILista(ListAPIView):
    #serializer_class = PersonaSerializer
    # serializer_class = PersonaSerializer2
    serializer_class = PersonaSerializer3
    def get_queryset(self):
        return Person.objects.all()

#### distinto serializer
class ReunionAPILista(ListAPIView):
    serializer_class = ReunionSerializer
    # serializer_class = ReunionSerializer2
    def get_queryset(self):
        return Reunion.objects.all()

class ReunionAPIListaLink(ListAPIView):
    serializer_class = ReunionSerializerLink
    def get_queryset(self):
        return Reunion.objects.all()