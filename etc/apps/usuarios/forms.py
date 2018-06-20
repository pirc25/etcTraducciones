from django import forms
from django.forms import widgets
from apps.usuarios.models import *
from django.forms.widgets import SelectDateWidget

"""
class CotizacionForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'type':'string','placeholder':'Nombre'}),label='Ingresa tu nombre',max_length=50)
    numero = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono o Celular'}),label='Ingresa tu numero telefonico o celular',max_length=10)
    email =  forms.EmailField(widget=forms.TextInput(attrs={'Correo Electronico':'Nombre'}),label='Ingresa tu correo electronico',max_length=30)
    texto =  forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Pega el texto a traducir'}),label='Ingresa el texto a traducir',max_length=1000,required=False)
    archivo= forms.FileField(label='Sube el archivo',required=False)


    def clean(self):
    	texto = self.cleaned_data.get('texto')
    	archivo = self.cleaned_data.get('archivo')
    	print (archivo)
    	if not texto and not archivo:
    		msg = forms.ValidationError("Se deben llenar los campos.")
    		self.add_error('texto', msg)

    	if texto and archivo:
    		print ('archivo')
    		msg = forms.ValidationError("Solo se debe pegar texto o subir un archivo.")
    		self.add_error('texto', msg)
    		self.add_error('archivo', msg)
    	elif texto:
        	self.cleaned_data['archivo'] = None
    	elif archivo:
        	self.cleaned_data['texto'] = None

    	return self.cleaned_data
"""

"""
class ClienteSignUpForm(forms.ModelForm):
	texto =  forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Pega el texto a traducir'}),label='Ingresa el texto a traducir',max_length=1000,required=False)
	archivo= forms.FileField(label='Sube el archivo',required=False)
	idioma = forms.ModelChoiceField(
        queryset=Idioma.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

	class Meta:
		model= Cliente

		fields = [
			'nombre',
			'apellido',
			'telefono',
			'email',
		]

		labels = {
			'nombre':'Nombre',
			'apellido':'Apellido',
			'telefono':'Telefono',
			'numero':'Telefono',
			'email':'Email',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}) ,
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			
		}

	def save(self):
		
		cliente = Cliente.objects.create(
			nombre=self.cleaned_data.get('nombre'),
			apellido=self.cleaned_data.get('apellido'),
			telefono=self.cleaned_data.get('telefono'),
			email=self.cleaned_data.get('email'),
			idioma=self.cleaned_data.get('idioma'))
		cliente.save()
		cliente=Cliente.objects.get(email=self.cleaned_data.get('email'))
		documento=Documento.objects.create(
			file=self.cleaned_data.get('archivo'),
			autor=cliente)
		documento.save()


		return cliente
"""

class CotizacionForm(forms.Form):
	titulo = forms.CharField(widget=forms.TextInput(attrs={'type':'string','placeholder':'Titulo'}),label='Titulo del documento',max_length=50)
	nombre = forms.CharField(widget=forms.TextInput(attrs={'type':'string','placeholder':'Nombre'}),label='Ingresa tu nombre',max_length=50)
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono o Celular'}),label='Ingresa tu numero telefonico o celular',max_length=10)
	email =  forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Correo electronico'}),label='Ingresa tu correo electronico',max_length=30)
	fecha_limite=forms.DateField(label='Fecha limite de entrega',widget=forms.TextInput(attrs={'class':'datepicker'}))

	idioma_origen = forms.ModelChoiceField(
        queryset=Idioma.objects.all(),
        widget=forms.Select(),
        required=True,
        empty_label=None)

	idioma_destino = forms.ModelChoiceField(
        queryset=Idioma.objects.all(),
        widget=forms.Select(),
        required=True,
        empty_label=None)
	archivo= forms.FileField(label='Sube el archivo',required=False)
	texto =  forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Pega el texto a traducir'}),label='Ingresa el texto a traducir',max_length=500,required=False)
	comentario= forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Deja un comentario'}),label='Comentario o Instruccion',max_length=150,required=False)
	


	
	def save(self):
		
		cotizacion = Cotizacion.objects.create(
			nombres=self.cleaned_data.get('nombre'),
			titulo=self.cleaned_data.get('titulo'),
			telefono=self.cleaned_data.get('telefono'),
			email=self.cleaned_data.get('email'),
			file=self.cleaned_data.get('archivo'),
			idioma_origen=self.cleaned_data.get('idioma_origen'),
			idioma_destino=self.cleaned_data.get('idioma_destino'),
			fecha_limite=self.cleaned_data.get('fecha_limite'),
			comentario=self.cleaned_data.get('comentario'))
		cotizacion.save()


		return cotizacion


	def clean(self):
		texto = self.cleaned_data.get('texto')
		archivo = self.cleaned_data.get('archivo')
		print (archivo)
		if not texto and not archivo:
			msg = forms.ValidationError("Se deben llenar los campos.")
			self.add_error('texto', msg)
		if texto and archivo:
			print ('archivo')
			msg = forms.ValidationError("Solo se debe pegar texto o subir un archivo.")
			self.add_error('texto', msg)
			self.add_error('archivo', msg)
		elif texto:
			self.cleaned_data['archivo'] = None
		elif archivo:
			self.cleaned_data['texto'] = None

		return self.cleaned_data