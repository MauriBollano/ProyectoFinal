from django import forms
from .models import *
from datetime import datetime
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PIL import Image

""" El nombre del formulario debe ser distinto al de la vista """

class RecetasForm(forms.Form):

    nombre = forms.CharField(label="Nombre")
    tipo_opciones = [
        (1, "Vegetariano"),
        (2, "Vegano"),
        (3, "Con carne"),
        (4,"Free Gluten")
    ]
    tipo = forms.ChoiceField(label="Tipo", choices=tipo_opciones)
    tiempo =  forms.IntegerField(label="Tiempo")
    dificultad_opciones= [
        (1,"Facil"),
        (2,"Media"),
        (3,"Dificil")
    ]

    dificultad= forms.ChoiceField(label="Dificultad", choices=dificultad_opciones)
    ingredientes = forms.CharField(label="Ingredientes", widget=CKEditorWidget)
    instrucciones = forms.CharField(label="Instrucciones",widget=CKEditorWidget)
    fecha = forms.DateTimeField(label="Fecha", initial=datetime.now, widget=forms.SelectDateWidget())
    imagen = forms.ImageField( label="Imagen",required=False)


class BlogForm(forms.Form):
    titulo = forms.CharField(label="Titulo")
    subtitulo = forms.CharField(label="Subtitulo")
    cuerpo = forms.CharField(label="Cuerpo", widget=CKEditorWidget)
    autor = forms.CharField(label="Autor")
    fecha = forms.DateField(label="Fecha", initial=datetime.now, widget=forms.SelectDateWidget())
    imagen = forms.ImageField( label="Imagen", required=False)
