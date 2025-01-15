from django.contrib import admin
from escola.models import Estudante, Cursos, Matricula

class Estudantes(admin.ModelAdmin):
  list_display = ('id','nome', 'email', 'cpf', 'data_nascimento', 'celular')
  list_display_links = ('id', 'nome' )
  list_per_page = 20
  search_fields = ('nome',)

admin.site.register(Estudante, Estudantes)

class Curso(admin.ModelAdmin):
  list_display = ('id','codigo', 'descricao')
  list_display_links = ('id', 'codigo' )

admin.site.register(Cursos, Curso)

class Matriculas(admin.ModelAdmin):
  list_display = ('id','estudante','curso','periodo')
  list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)