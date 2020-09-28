from django.shortcuts import render
from django.db.models import Count, Sum
from django.db import models
from .models import Consulta
from .models import Exame

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):

    qs = Consulta.objects.all()
    nome_medico = request.GET.get('nome_medico')
    data_inicio = request.GET.get('data_inicio')
    data_fim    = request.GET.get('data_fim')

    if is_valid_queryparam(nome_medico):
        qs = qs.filter(nome_medico__iexact=nome_medico)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
        for q in qs:
            print(q.numero_guia,q.num_exame,q.total)

    if is_valid_queryparam(data_inicio) and is_valid_queryparam(data_fim):
        qs = qs.filter(data_consulta__range=[data_inicio,data_fim])
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
    elif is_valid_queryparam(data_inicio):
        qs = qs.filter(data_consulta__gte=data_inicio)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
    elif is_valid_queryparam(data_fim):
        qs = qs.filter(data_consulta__lt=data_fim)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))

    return qs

def consulta_list(request):
   
    if request:
        qs = filter(request)
    else:
        qs = []

    context = {
        'consultas': qs,
        'medicos': Consulta.objects.all(),
    }

    return render(request,"list.html", context)