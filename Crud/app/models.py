from django.db import models
from app.enums.estadoCurso import EstadoCurso

class Egressos(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, unique=True)
    nome = models.CharField(max_length=80)
    tel = models.CharField(max_length=14)
    email = models.CharField(max_length=80)
    curso = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=EstadoCurso.choices)
    profissao_atual = models.CharField(max_length=50)
    empresa_atual = models.CharField(max_length=50)
    deseja_parcerias = models.BooleanField(default=False)  
    deseja_partEvent = models.BooleanField(default=False) 
    deseja_fazerNewCursos = models.BooleanField(default=False)  