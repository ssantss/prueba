from django.conf.urls import patterns,url

urlpatterns = patterns('generador.apps.home.views',
    url(r'^$','index_view',name='vista_index'),
    url(r'^login/$','login_view',name='login_view'),
    url(r'^logout/$','logout_view',name='logout_view'),
    url(r'^gestion_users/$','gestion_users_view',name='gestion_users_view'),
)