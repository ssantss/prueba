from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.contrib.auth.models import User
from generador.apps.home.models import Usuario

def index_view(request):
	if request.user.is_authenticated():
		return render_to_response('index.html', locals(), context_instance=RequestContext(request))
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
				return render_to_response('login.html',locals(),context_instance=RequestContext(request))
		return render_to_response('login.html',locals(),context_instance=RequestContext(request))

def logout_view(request):
        logout(request)
        return HttpResponseRedirect('/')
        

def gestion_users_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			users = Users.objects.all()
			return render_to_response('users.html',ctx,context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def edit_user_view(request,id_user):
	if request.user.is_authenticated():
		if request.user.is_staff:
			try:
				user = User.objects.get(id=id_user)
				if request.method == "POST":
					if user:
						user.firs_name = request.POST['firs_name']
						user.username = request.POST['username']
						user.password = request.POST['password']
						user.email = request.POST['email']
						user.save()
						return HttpResponseRedirect('/')
				else:
					ctx = {'user':user}
					return render_to_response('edit_user.html',ctx,context_instance=RequestContext(request))
			except User.DoesNotExist:
				return HttpResponseRedirect('/')
						


def register_view(request):
    if request.user.is_authenticated():
		if request.user.is_staff:
		    if request.method == "POST":
		        usuario = request.POST['username']
		        email = request.POST['email']
		        password_one = request.POST['password_one']
		        password_two = request.POST['password_two']
		        u = User(username=usuario,email=email,password=password_one)
		        u.save()
		        return render_to_response('succes_register.html',context_instance=RequestContext(request))
		    else: