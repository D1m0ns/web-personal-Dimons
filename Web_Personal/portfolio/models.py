from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to= "projects")
    link = models.URLField(verbose_name = "Enlace", max_length=200, blank= True, null= True )
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering =["-created"]
    def __str__(self):
        return self.title
    