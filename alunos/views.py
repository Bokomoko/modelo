from django.shortcuts import render
from .models import Aluno

# Create your views here.


def index(request):
    return render(request,  # request object
                  'paginaalunos/index.html',  # the page to render
                  {'alunos': Aluno.objects.all()},  # a context dictionary
                  )

# the method objects.all return dictionary with all attributes of the entity Aluno
