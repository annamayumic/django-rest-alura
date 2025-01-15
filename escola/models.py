from django.db import models

class Estudante(models.Model):
  nome = models.CharField(max_length=100)
  email = models.CharField(max_length=30, blank=False)
  cpf = models.CharField(max_length=11)
  data_nascimento = models.DateField()
  celular = models.CharField(max_length=14)

  def __str__(self):
    return self.nome


class Cursos(models.Model):

  OPCOES_NIVEL =(('B','Básico'),('I','Intermediário'),('A','Avançado'))

  codigo = models.CharField(max_length=10)
  descricao = models.CharField( max_length=100, blank=False)
  Nivel = models.CharField(default='B', choices=OPCOES_NIVEL, blank=False, null=False, max_length=15)

  def __str__(self):
    return self.codigo

class Matricula(models.Model):
#many to one, Estudantes tem many matriculas, matricula tem One estudante
    OPCOES_PERIODO = (
      ('M','Matutino'), 
      ('V','Vespertino'), 
      ('N','Noturno'),
      )

    estudante = models.ForeignKey(Estudante,on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
    periodo = models.CharField(choices = OPCOES_PERIODO, blank=False, null=False, max_length=20, default='M')

