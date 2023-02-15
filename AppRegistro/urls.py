from django.urls import path
from AppRegistro import views
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('agregar_url/', views.agregar_url, name='agregar_url'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('agregar_avatar/', views.agregar_avatar, name='agregar_avatar'),
    path('agregar_descripcion/', views.agregar_descripcion, name='agregar_descripcion'),
]