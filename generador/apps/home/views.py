from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.contrib.auth.models import User
from generador.apps.home.models import Usuario

def index_view(request):
	if request.user.is_authenticated():
		return render_to_response('home/index.html', locals(), context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			usuario = authenticate(username = username, password = password)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return HttpResponseRedirect('/')
			else:
				mensaje = "usuario y/o password incorrecto"
				return render_to_response('home/login.html',locals(),context_instance=RequestContext(request))
		return render_to_response('home/login.html',locals(),context_instance=RequestContext(request))

def logout_view(request):
        logout(request)
        return HttpResponseRedirect('/')
        

def gestion_users_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			users = User.objects.filter(is_active=True)
			ctx = {'users':users}
			return render_to_response('home/users.html',ctx,context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def register_user_view(request):
    if request.user.is_authenticated():
		if request.user.is_staff:
		    if request.method == "POST":
		        username = request.POST['username']
		        email = request.POST['email']
		        first_name = request.POST['first_name']
		        password_one = request.POST['password_one']
		        #password_two = request.POST['password_two']
		        try:
		        	if request.POST['super']:
		        		staff = True
		        except:
		        	staff = False

		        try:
		        	 u = User.objects.get(email = email)
		        	 if u.DoesNotExist:
		        	 	return render_to_response('home/email_repetido.html',locals(),context_instance=RequestContext(request))
		        except User.DoesNotExist:
			        try:
			        	u = User.objects.get(username=username)
			        except User.DoesNotExist:
			        	if staff:
			        		usuario = User.objects.create_superuser(username=username,password=password_one,email=email,first_name=first_name)
			        	else:
				        	usuario = User.objects.create_user(username=username,password=password_one,email=email,first_name=first_name)
				        	usuario.save()
				        	return HttpResponseRedirect('/success_register_user/')

			    	return render_to_response('home/user_exist.html',locals(),context_instance=RequestContext(request))
		    else:
		    	return render_to_response('home/register_user.html',locals(),context_instance=RequestContext(request))


def edit_user_view(request,id_user):
	if request.user.is_authenticated():
		if request.user.is_staff:
			try:
				usuario = User.objects.get(id=id_user)
				if request.method == "POST":
					try:
						if request.POST['super']:
							staff = True
					except:
						staff = False
					first_name = request.POST['first_name']
					password_one = request.POST['password_one']
					password_two = request.POST['password_two']
					if password_one == password_two:
						pass
					else:
						return render_to_response('home/bug_contrasenas.html',locals(),context_instance=RequestContext(request))
					if usuario:
						if staff:
							usuario.first_name = first_name
							usuario.set_password(password_one)
							usuario.email = request.POST['email']
							usuario.is_staff = True
							usuario.save()
							return HttpResponseRedirect('/success_register_user/')
						else:
							usuario.first_name = first_name
							usuario.password = password_one
							usuario.email = request.POST['email']
							usuario.is_staff = False
							usuario.save()
							return HttpResponseRedirect('/success_register_user/')
				else:
					ctx = {'usuario':usuario}
					return render_to_response('home/edit_user.html',ctx,context_instance=RequestContext(request))
			except User.DoesNotExist:
				return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')						



def delete_user_view(request,id_user):
	if request.user.is_authenticated():
		if request.user.is_staff:
			try:
				user = User.objects.get(id = id_user)
				user.delete()
			except User.DoesNotExist:
				return HttpResponseRedirect("/")
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def admin_user_view(request,id_user):
	if request.user.is_authenticated():
		if request.user.is_staff:
			usuario = User.objects.get(id=id_user)			
			return render_to_response('home/admin_user.html',locals(),context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def success_register_user_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			return render_to_response('home/success_register_user.html',locals(),context_instance=RequestContext(request))