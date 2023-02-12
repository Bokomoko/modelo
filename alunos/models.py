from django.db import models

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.EmailField()
    campo_de_estudo = models.CharField(max_length=100)
    discordid = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome + ' - ' + self.nickname
