from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, redirect
from .forms import PersonForm

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

#Funciones del CRUD
#Create
def user_form(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_one')

    context = {'form':form}
    return render(request, 'form.html', context)

#Update
def user_update(request, pk):
    person = Person.objectes.get(id = pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('index_one')
        
    context = {'form':form}
    return render(request, 'form.html', context)

#Delete
def user_delete(request, pk):
    person = Person.objectes.get(id = pk)

    if request.method == 'POST':
        person.delete()
        return redirect('index_one')
        
    context = {'object':person}
    return render(request, 'delete_object.html', context)







