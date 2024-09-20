from django.forms import ModelForm
from app.models import Egressos

class EgressosForm(ModelForm):
    class Meta:
        model = Egressos
        fields = ['cpf', 'nome', 'tel', 'email', 'curso', 'estado', 'profissao_atual', 'empresa_atual', 'deseja_parcerias','deseja_partEvent', 'deseja_fazerNewCursos' ]
