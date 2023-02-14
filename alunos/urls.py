from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:aluno_id>/', views.view_aluno, name='view_aluno'),
    path('add/', views.add, name='add'),
]
