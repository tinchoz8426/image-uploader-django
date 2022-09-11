from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="images") # https://docs.djangoproject.com/en/4.1/ref/models/fields/#imagefield
    date = models.DateTimeField(auto_now_add=True) # https://docs.djangoproject.com/en/4.1/ref/models/fields/#datetimefield  --> Importante!! Tambien tenemos DateField que es solamente una fecha y tambien tenemos TimeField que es un horario.
    # Otro dato importante es la diferencias entre auto_now_add y auto_now --> https://stackoverflow.com/questions/51389042/difference-between-auto-now-and-auto-now-add
    
    # archivo = models.FileField() # Lo puse para probar la multicarga de archivos.

    def __str__(self):
        return self.name