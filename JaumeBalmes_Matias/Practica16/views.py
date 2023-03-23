from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index_one(request):
    return HttpResponse('uhuhh World')

professors = [
    {
        'id':'1',
        'name':'Matias',
        'surname':'Rodriguez',
        'edad':'20'
    },
    {
        'id':'2',
        'name':'Roger',
        'surname':'Sobrino',
        'edad':'20'
    },
    {
        'id':'3',
        'name':'Raul',
        'surname':'Rufo',
        'edad':'20'
    }
]

def teachers(request):
    context = {'profs': professors}
    return render(request, 'professors.html', context)

alumnos = [
    {
        'id':'1',
        'name':'Matias',
        'surname':'Rodriguez',
        'edad':'20'
    },
    {
        'id':'2',
        'name':'Roger',
        'surname':'Sobrino',
        'edad':'20'
    },
    {
        'id':'3',
        'name':'Raul',
        'surname':'Rufo',
        'edad':'20'
    },
    {
        'id':'4',
        'name':'Patito',
        'surname':'Milet',
        'edad':'20'
    },
    {
        'id':'5',
        'name':'Andres',
        'surname':'Carles',
        'edad':'20'
    },
    {
        'id':'6',
        'name':'Miquel',
        'surname':'Montoro',
        'edad':'20'
    }
]

def students(request):
    context = {'alumns': alumnos}
    return render(request, 'alumnos.html', context)

