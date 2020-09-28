from django.db import models

# Create your models here.
class Consulta(models.Model):
    numero_guia = models.IntegerField()
    cod_medico = models.IntegerField()
    nome_medico = models.TextField(max_length=100)
    data_consulta = models.DateField()
    valor_consulta = models.DecimalField(max_digits=5, decimal_places=2)

class Exame(models.Model):
    numero_guia_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    exame = models.TextField(max_length=100)
    valor_exame = models.DecimalField(max_digits=5,decimal_places=2)

