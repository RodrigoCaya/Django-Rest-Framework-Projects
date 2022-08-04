from django.urls import path, re_path
from . import views

app_name = 'persona_app'
urlpatterns = [
    path('personas/', views.ListaPersonas.as_view(), name='personas'),
    path('api/persona/lista/', views.PersonListApiView.as_view()), #para verlo como json puro, colocar api/personas/list/?format=json
    path('lista/', views.PersonListView.as_view(), name='lista'),
    path('api/persona/search/<kword>/', views.PersonSearchApiView.as_view()),
    path('api/persona/create/', views.PersonCreateView.as_view()),
    path('api/persona/detail/<pk>/', views.PersonRetrieveView.as_view(), name='detalle'),
    path('api/persona/delete/<pk>/', views.PersonDeleteView.as_view()),
    path('api/persona/update/<pk>/', views.PersonUpdateView.as_view()),
    path('api/persona/modificar/<pk>/', views.PersonRetrieveUpdateView.as_view()),
    #nuevo serializer
    path('api/personas/', views.PersonAPILista.as_view()),
    path('api/reuniones/', views.ReunionAPILista.as_view()),
    path('api/reuniones-link/', views.ReunionAPIListaLink.as_view()),
]