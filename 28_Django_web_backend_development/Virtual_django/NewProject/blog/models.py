from django.db import models

# Create your models here.
class Post(models.Model):
    # verbose_name is how the input will be show 
    title = models.CharField(max_length=200, verbose_name="Título") 
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Modificado")

    class Meta:
        # Metadata field, with the names for input in singular and plural
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        #redefine the str name, returning the name of the input not the object
        return self.title