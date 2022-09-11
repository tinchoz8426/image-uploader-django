from django import forms
from django.forms.widgets import TextInput

from .models import Image

class ImageForm(forms.ModelForm):

    name = forms.CharField(widget=TextInput(attrs={'class':'photo-name','placeholder': 'Nombre de la imagen'}), label="")
    # archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})) # Si quiero cargar multiples archivos --> https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/#uploading-multiple-files

    class Meta:
        model = Image
        fields = "__all__"
        labels = {'photo': '', 'name': ''} # Para cambiar en nombre de los labels en el fomulario del html