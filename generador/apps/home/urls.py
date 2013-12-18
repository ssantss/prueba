from django.conf.urls import patterns,url

urlpatterns = patterns('generador.apps.home.views',
    url(r'^$','index_view',name='vista_index'),
    url(r'^login/$','login_view',name='login_view'),
    url(r'^logout/$','logout_view',name='logout_view'),
    url(r'^gestion_users/$','gestion_users_view',name='gestion_users_view'),
    #url(r'^users/(?P<username>.*)/$','users_view',name='users_view'),
    url(r'^edit/user/(?P<id_user>.*)/$','edit_user_view',name='vista_edit_user'),
    url(r'^delete/user/(?P<id_user>.*)/$','delete_user_view',name='vista_delete_user'),
    url(r'^register_new_user/$','register_user_view',name='view_register_user'),
    url(r'^success_register_user/$', 'success_register_user_view', name='view_success_user'),
    url(r'^admin/user/(?P<id_user>.*)/$', 'admin_user_view', name='view_admin_user'),
)