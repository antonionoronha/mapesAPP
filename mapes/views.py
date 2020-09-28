from django.shortcuts import render
from django.db.models import Count, Sum
from django.db import models
from .models import Consulta
from .models import Exame

def is_valid_queryparam(param):
    return param != '' and param is not None

def consulta_list(request):

    medicos = Consulta.objects.all()
    qs = Consulta.objects.all()
    nome_medico = request.GET.get('nome_medico')
    data_inicio = request.GET.get('data_inicio')
    data_fim    = request.GET.get('data_fim')

    if is_valid_queryparam(nome_medico):
        qs = qs.filter(nome_medico__iexact=nome_medico)
        #print(qs[0])
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
        #print(qs[1].total)
        for q in qs:
            print(q.numero_guia,q.num_exame,q.total)

    if is_valid_queryparam(data_inicio) and is_valid_queryparam(data_fim):
        qs = qs.filter(data_consulta__range=['2020-09-27','2019-01-01'])
        print(qs)
        #qs = qs.filter(data_consulta__range=[data_inicio,data_fim])
    elif is_valid_queryparam(data_inicio):
        qs = qs.filter(data_consulta__year__gte=2019)
    elif is_valid_queryparam(data_fim):
        qs = qs.filter(data_consulta__lt='2020-09-27')
        print(qs)
        print(data_fim)

    context = {
        'consultas': qs,
        'medicos': medicos,
    }

    return render(request,"list.html", context)