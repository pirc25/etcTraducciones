
from django.conf import settings
import os
from docx import Document

def handle_uploaded_file(f,nombre):
    with open(settings.MEDIA_ROOT+"/files/"+str(nombre),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def contadorPalabras(nombre):
	document = Document(settings.MEDIA_ROOT+"/files/"+str(nombre))
	total=0
	for p in document.paragraphs:
		total=total+len(p.text.split())
		#print (str(p.text.split())+":"+str(len(p.text.split())))

	return total


def contarTXT(string):
	char=0
	word=1
	for i in string:
		char=char+1
		if(i==' '):
			word=word+1
	
	return word

def crearTXT(texto,nombre):
	f = open (settings.MEDIA_ROOT+"/files/"+str(nombre),'w')
	f.write(texto)
	f.close()