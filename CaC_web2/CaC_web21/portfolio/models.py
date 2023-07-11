from django.db import models

# Create your models here. Están basadas en clases (deben ser nombres en singular)
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Títulos")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imágen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Meta:
    verbose_name = "proyecto"
    verbose_name = "proyectos"
    ordering=['-created']