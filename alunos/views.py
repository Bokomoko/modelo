from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Aluno

# Create your views here.


def index(request):
    return render(request,  # request object
                  'paginaalunos/index.html',  # the page to render
                  {'alunos': Aluno.objects.all()},  # a context dictionary
                  )

# create a view to show the Aluno detail page


def view_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    return HttpResponseRedirect(reverse('paginaalunos'))
