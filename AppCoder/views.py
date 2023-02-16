from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import *
from AppCoder.forms import *
from AppRegistro.forms import *
from AppRegistro.views import *
from PIL import Image
from AppRegistro.views import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def inicio (request):
    ultimas_recetas = Recetas.objects.order_by('-fecha')[:2]
    ultimos_blogs = Blog.objects.order_by('-fecha')[:2]
    context = {
        'ultimas_recetas': ultimas_recetas,
        'ultimos_blogs': ultimos_blogs
    }

    if request.user.is_authenticated:
        avatar = obtener_avatar(request)
        context['avatar'] = avatar

    return render(request, 'AppCoder/inicio.html', context)


def aboutMe(request):

    if request.user.is_authenticated:
        return render(request, 'AppCoder/aboutMe.html', {'avatar': obtener_avatar(request)})
    else:
        return render(request, 'AppCoder/aboutMe.html')



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


@method_decorator(login_required, name='dispatch')
class RecetasCreacion(CreateView):

    model = Recetas
    success_url = reverse_lazy('Recetas')
    fields = ['nombre', 'tipo','tiempo','dificultad','ingredientes','instrucciones','imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = obtener_avatar(self.request)
        return context

@method_decorator(login_required, name='dispatch')
class RecetasUpdate(UpdateView):

    model = Recetas
    succes_url = reverse_lazy('Recetas')
    fields = ['nombre', 'tipo','tiempo','dificultad','ingredientes','instrucciones','imagen']

    def get_success_url(self):
        return reverse('RecetasLista')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = obtener_avatar(self.request)
        return context

@method_decorator(login_required, name='dispatch')
class RecetasDelete(DeleteView):

    model = Recetas
    success_url = reverse_lazy('Recetas')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = obtener_avatar(self.request)
        return context


""" Clases basada em vosta para los post """

class BlogLista(ListView):

    model = Blog
    template_name = 'AppCoder/blog_list.html'
    ordering = ['-fecha']


class BlogDetalles(DetailView):

    model = Blog
    template_name = 'AppCoder/blog_detalle.html'


@method_decorator(login_required, name='dispatch')
class BlogCreacion(CreateView):

    model = Blog
    success_url = reverse_lazy('Blog')
    fields = ['titulo','subtitulo','resumen','cuerpo','autor','imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = obtener_avatar(self.request)
        return context

@method_decorator(login_required, name='dispatch')
class BlogUpdate(UpdateView):

    model = Blog
    succes_url = reverse_lazy('Blog')
    fields = ['titulo','subtitulo','resumen','cuerpo','autor','imagen']

    def get_success_url(self):
        return reverse('Blog')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = obtener_avatar(self.request)
        return context

@method_decorator(login_required, name='dispatch')
class BlogDelete(DeleteView):

    model = Blog
    success_url = reverse_lazy('Blog')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = obtener_avatar(self.request)
        return context




