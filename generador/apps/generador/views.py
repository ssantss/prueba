from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect

def upload_file_view(request):
	if request.method == 'POST':
		archivo = request.FILES["archivo"].read()		
		lista1 = archivo.split("{\n")

		listaTabla = lista1[0].split(' ')

		listaCampos = lista1[1].split(',\n')
		del listaCampos[-1] 	

		index = 0

		for campo in listaCampos:
			camposDic = dict()
			lista_to_dic = campo.split(' ')
			for x in lista_to_dic:
				camposDic['nombre'] = lista_to_dic[0]
				camposDic['tipo'] = lista_to_dic[1]
				try:
					if lista_to_dic[2]:
						camposDic['llave'] = lista_to_dic[2]
				except:
					print "no esllave"				
				

			listaCampos[index] = camposDic
			index+=1

		print 'nombre de la tabla : '+listaTabla[2]
		print 'campos : '
		for campo in listaCampos:
			print 'nombre :'+ campo['nombre']
			print 'tipo de dato: '+ campo['tipo']
			
			try:
				if campo['llave']:
					print 'llave: '+ campo['llave']
			except:
				pass
			
			print '-------------------------------------'
	return render_to_response('generador/upload_file.html', locals(), context_instance=RequestContext(request))
