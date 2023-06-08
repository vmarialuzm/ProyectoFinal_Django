from django.db import models

class Proyecto(models.Model):
    foto = models.URLField()
    titulo_proyecto = models.CharField(max_length=200) 
    descripcion_proyecto = models.TextField()
    tags = models.CharField(max_length=200)
    url_github = models.URLField()

    class Meta:
        db_table = "proyecto"


