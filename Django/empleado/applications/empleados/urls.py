from django.urls import path
from . import views

urlpatterns = [
    path('listar-todos-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<name_url>/', views.ListByAreaEmpleados.as_view()),
    path('listar-by-job/<name_url>/', views.ListByJobEmpleados.as_view()),
    path('buscar-empleado/', views.ListByKeyWordEmpleados.as_view()),
]