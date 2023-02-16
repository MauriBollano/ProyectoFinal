from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Recetas(models.Model):

    TIPO_OPCIONES = [
        (1, "Vegetariano"),
        (2, "Vegano"),
        (3, "Contiene carne"),
        (4, "Free Gluten")
    ]

    DIFICULTAD_OPCIONES= [
        (1,"Facil"),
        (2,"Media"),
        (3,"Dificil")
    ]

    nombre = models.CharField(max_length=40);
    tipo = models.IntegerField(null=False,blank=False,choices= TIPO_OPCIONES)
    tiempo =  models.IntegerField()
    dificultad = models.IntegerField(null=False,blank=False, choices= DIFICULTAD_OPCIONES)
    ingredientes = RichTextField()
    instrucciones = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True,blank=True, upload_to= "imagenes/")
    
    def get_tipo_display(self):
        for tipo in self.TIPO_OPCIONES:
            if self.tipo == tipo[0]:
                return tipo[1]
        return None

    def get_dificultad_display(self):
        for opcion in self.DIFICULTAD_OPCIONES:
            if self.dificultad == opcion[0]:
                return opcion[1]
        return None

    def save(self, *args, **kwargs):
        if not self.imagen:
            self.imagen = 'imagenes/RecetasDefaultIMG.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre +" "+ str(self.tipo)

class Blog(models.Model):
    titulo = models.CharField(max_length = 50)
    subtitulo = models.CharField(max_length = 100)
    resumen= RichTextField(null=True)
    cuerpo = RichTextField()
    autor = models.CharField(max_length = 50)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(null=True,blank=True,  upload_to= "imagenes/")
    
    def save(self, *args, **kwargs):
        if not self.imagen:
            self.imagen = 'imagenes/BlogDefaultIMG.jpg'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return "Titulo : " + self.titulo + " -  Subtitulo: " + self.subtitulo + " -  Autor: " + self.autor