from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import *
from AppCoder.forms import *
from PIL import Image
from AppRegistro.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio (request):
    if request.user.is_authenticated:
        return render(request, 'AppCoder/inicio.html', {'avatar': obtener_avatar(request)})
    else:
        return render(request, 'AppCoder/inicio.html')

def aboutMe(request):

    return render(request, 'AppCoder/aboutMe.html')



def blog(request):


    if request.method == "POST":

        miFormulario = BlogForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            blog = Blog(titulo=informacion["titulo"], subtitulo=informacion["subtitulo"], cuerpo=informacion["cuerpo"],autor=informacion["autor"],fecha=informacion["fecha"], imagen="imagen")
            blog.save()
            return render(request, "AppCoder/inicio.html")
    else:
            miFormulario = BlogForm()

    return render(request, "AppCoder/blog.html", {"miFormulario": miFormulario})


def busquedaRecetas(request):
    return render(request, "AppCoder/busquedaRecetas.html")

def buscarRecetas(request):
    
    if request.GET["nombre"]:
            nombre=request.GET["nombre"]
            if len(nombre)>25:
                respuesta="Nombre demasiado largo"
            else:
                nombrereceta = request.GET['nombre']
                rec=Recetas.objects.filter(nombre__icontains= nombrereceta)
            
                return render(request, "AppCoder/resultadoBusqueda.html",{"rec":rec, "query":nombrereceta})
    else:
            respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)


""" Classes basadas en vistas para el modelo Recetas """

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

class RecetasLista(ListView):

    model = Recetas
    template_name = 'AppCoder/recetas_list.html'

class RecetasDetalles(DetailView):

    model = Recetas
    template_name = 'AppCoder/recetas_detalle.html'


class RecetasCreacion(CreateView):

    model = Recetas
    success_url = reverse_lazy('Recetas')
    fields = ['nombre', 'tipo','tiempo','dificultad','ingredientes','instrucciones','imagen']


class RecetasUpdate(UpdateView):

    model = Recetas
    succes_url = reverse_lazy('Recetas')
    fields = ['nombre', 'tipo','tiempo','dificultad','ingredientes','instrucciones','imagen']

    def get_success_url(self):
        return reverse('RecetasLista')


class RecetasDelete(DeleteView):

    model = Recetas
    success_url = reverse_lazy('Recetas')

""" Clases basada em vosta para los post """

class BlogLista(ListView):

    model = Blog
    template_name = 'AppCoder/blog_list.html'

class BlogDetalles(DetailView):

    model = Blog
    template_name = 'AppCoder/blog_detalle.html'


class BlogCreacion(CreateView):

    model = Blog
    success_url = reverse_lazy('Blog')
    fields = ['titulo','subtitulo','cuerpo','autor','imagen']


class BlogUpdate(UpdateView):

    model = Blog
    succes_url = reverse_lazy('Blog')
    fields = ['titulo','subtitulo','cuerpo','autor','imagen']

    def get_success_url(self):
        return reverse('Blog')


class BlogDelete(DeleteView):

    model = Blog
    success_url = reverse_lazy('Blog')




