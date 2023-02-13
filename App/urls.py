from django.urls import path
from . import views

urlpatterns = [
    path('',views.nome_da_função, name='nome da funcao'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('Info/',views.info,name='info')
]