from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index_one(request):
    return HttpResponse('uhuhh World')

def teachers(request):
    professor = {'name':'Matias','surname':'Rodriguez','edad':'20'}
    template = loader.get_template('index.html')
    dades = template.render({'name':professor['name'], 'surname':professor['surname'], 'edad':professor['edad']})
    return HttpResponse(dades)
    # return render(request, 'index.html', {'name':professor['name'], 'surname':professor['surname'], 'edad':professor['edad']})
