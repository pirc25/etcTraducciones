
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

"""
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
"""
from django.views.generic import CreateView,TemplateView,ListView,FormView,RedirectView
from django.urls import reverse_lazy

#from apps.usuarios.models import *
from apps.usuarios.forms import *
from apps.usuarios.models import *



from apps.usuarios.helpers import handle_uploaded_file, contadorPalabras, crearTXT, contarTXT






def cotizar(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            try:
                if form.cleaned_data.get('texto'):
                    txt=form.cleaned_data.get('texto')
                    total=contarTXT(txt)
                    crearTXT(txt,form.cleaned_data.get('titulo'))
                    return render(request,'registro/respuesta.html',{'total':total})
                else:
                    total=contadorPalabras(request.FILES['archivo'].name)
                    #return HttpResponseRedirect('/')
                    return render(request,'registro/respuesta.html',{'total':total})
            except:
                return HttpResponseRedirect('/')
            
    else:
        form = CotizacionForm()
    return render(request, 'registro/cotizacion2.html', {'form': form})





"""
def cotizar(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST, request.FILES)
        if form.is_valid():
        	print('Entro')
        	if not form.cleaned_data.get('texto'):
        		handle_uploaded_file(request.FILES['archivo'],request.FILES['archivo'].name)
        		return HttpResponseRedirect('/')
        	else:
        		return HttpResponseRedirect('/')
    else:
        form = CotizacionForm()
    return render(request, 'registro/cotizacion2.html', {'form': form})

"""


"""
def cotizar(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST, request.FILES)
        if form.is_valid():
        	print('Entro')
        	handle_uploaded_file(request.FILES['archivo'],request.FILES['archivo'].name)
        	return HttpResponseRedirect('/')
    else:
        form = CotizacionForm()
    return render(request, 'registro/cotizacion2.html', {'form': form})
"""
"""
def upload_file(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['archivo'],request.FILES['archivo'].name)
            return HttpResponseRedirect('/')
    else:
        form = CotizacionForm()
    return render(request, 'registro/cotizacion2.html', {'form': form})
"""

