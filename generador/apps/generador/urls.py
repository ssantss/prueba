from django.conf.urls import patterns,url

urlpatterns = patterns('generador.apps.generador.views',
    url(r'^upload_file/$','upload_file_view',name='vista_upload'),
)