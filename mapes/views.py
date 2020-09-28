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

    #Utilizando os três parâmetros como consulta
    if is_valid_queryparam(nome_medico) and nome_medico != 'Escolha...' and is_valid_queryparam(data_inicio) and is_valid_queryparam(data_fim):
        qs = qs.filter(nome_medico__iexact=nome_medico)        
        qs = qs.filter(data_consulta__range=[data_inicio,data_fim])
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
    #Nome e data do início
    elif is_valid_queryparam(nome_medico) and nome_medico != 'Escolha...' and is_valid_queryparam(data_inicio):
        qs = qs.filter(nome_medico__iexact=nome_medico)
        qs = qs.filter(data_consulta__gte=data_inicio)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
    #Nome e data fim
    elif is_valid_queryparam(nome_medico) and nome_medico != 'Escolha...' and is_valid_queryparam(data_fim):
        qs = qs.filter(nome_medico__iexact=nome_medico)
        qs = qs.filter(data_consulta__lt=data_fim)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
        qs = qs.order_by('total')
    #Apenas o nome
    elif is_valid_queryparam(nome_medico) and nome_medico != 'Escolha...':
        qs = qs.filter(nome_medico__iexact=nome_medico)
        print(qs[0].cod_medico)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
        qs = qs.order_by('-total')
    #Data início e data fim
    elif is_valid_queryparam(data_inicio) and is_valid_queryparam(data_fim):
        qs = qs.filter(data_consulta__range=[data_inicio,data_fim])
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
    #Data início
    elif is_valid_queryparam(data_inicio):
        qs = qs.filter(data_consulta__gte=data_inicio)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))
    #Data fim
    elif is_valid_queryparam(data_fim):
        qs = qs.filter(data_consulta__lt=data_fim)
        qs = qs.annotate(num_exame=Count('exame'))
        qs = qs.annotate(total=Sum('exame__valor_exame'))

    return qs

def consulta_list(request):
    
    print(request)

    if request != '/':
        qs = filter(request)
    else:
        qs = []

    context = {
        'consultas': qs,
        'medicos': Consulta.objects.all(),
    }

    return render(request,"list.html", context)