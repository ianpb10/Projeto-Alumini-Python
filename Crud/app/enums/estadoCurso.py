from django.db import models

class EstadoCurso(models.TextChoices):
    FINALIZADO = 'FIN', 'Finalizado'
    INTERROMPIDO = 'INT', 'Interrompido'