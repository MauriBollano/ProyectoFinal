from django.urls import path, include
from .views import *
from django.contrib.auth. views import LogoutView


urlpatterns = [

    path('', inicio ,name="Inicio"),
    path('recetas',RecetasLista.as_view(),name='Recetas'),
    path('blog',BlogLista.as_view(),name='Blog'),
    path('busquedaRecetas',busquedaRecetas,name='BusquedaRecetas'),
    path('buscar/',buscarRecetas),
    path('aboutMe',aboutMe,name='AboutMe'),

    path('recetas/', include([
        path('list', RecetasLista.as_view(), name='RecetasLista'),
        path('<int:pk>/', RecetasDetalles.as_view(), name='RecetasDetalles'),
        path('nuevo/', RecetasCreacion.as_view(), name='RecetasCreacion'),
        path('editar/<int:pk>/', RecetasUpdate.as_view(), name='RecetasUpdate'),
        path('borrar/<int:pk>/', RecetasDelete.as_view(), name='RecetasDelete'),

    ])),

    path('blog/', include([
        path('list', BlogLista.as_view(), name='BlogLista'),    
        path('<int:pk>/', BlogDetalles.as_view(), name='BlogDetalles'),
        path('nuevo/', BlogCreacion.as_view(), name='BlogCreacion'),
        path('editar/<int:pk>/', BlogUpdate.as_view(), name='BlogUpdate'),
        path('borrar/<int:pk>/',BlogDelete.as_view(), name='BlogDelete'),
    ])),
]



