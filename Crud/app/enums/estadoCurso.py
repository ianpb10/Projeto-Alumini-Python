from django.db import models

class EstadoCurso(models.TextChoices):
    FINALIZADO = 'Finalizado', 'Finalizado'
    INTERROMPIDO = 'Interrompido', 'Interrompido'