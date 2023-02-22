from django.urls import path
from App import views

urlpatterns = [
    path('',views.nome_da_função, name='nome da funcao'),
    path('Cadastro/',views.cadastro,name='cadastro'),
    path('Info/<int:id>/',views.info,name='info')
]