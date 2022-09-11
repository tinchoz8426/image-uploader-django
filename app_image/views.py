from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView

from image_uploader.settings import STATIC_ROOT, STATICFILES_DIRS

from .models import Image
from .forms import ImageForm

# Create your views here.
def home(request):

    print(STATIC_ROOT)
    print(STATICFILES_DIRS)
    images = Image.objects.all()

    print(request.method) # Imprimo para ver que tipo de metodo es

    print(request) # Imprime <WSGIRequest: GET '/'> 
    
    print(dir(request)) # Imprime todos los metodos, funciones, etc que tiene request
    
    print(f"Este es el request.FILES --> {request.FILES}") # obviamente estara vacio porque todavia no cargue nada y no utilice el metodo POST

    if request.method == "POST":
        print(f"Este es el request.POST --> {request.POST}")

        print(f"Este es el request.FILES --> {request.FILES}")

        form = ImageForm(request.POST, request.FILES) # https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/#file-uploads
        #### Explicacion de porque van request.POST y request.FILES. ####
        # request.POST nos da los parametros del formulario tanto el csrfmiddlewaretoken como el name. Y request.FILES los archivos que cargue el usuario. Si eliminamos alguno de esos, cuando apretamos en "Subir imagen" nos va a decir que alguno de esos campos es requerido.
        
        print(form) # Formulario en crudo
        
        print(form.cleaned_data) # Trae el formulario limpio, y lo hace diccionario. Ejemplo --> {'name': 'blogcito', 'photo': <InMemoryUploadedFile: icon-blog.png (image/png)>}

        print(type(form.cleaned_data)) # Aca imprimo el tipo de dato de ese cleaned_data para ver que ES un diccionario

        # Esta respuesta en stackoverflow explica muy bien cleaned_data: https://stackoverflow.com/questions/53594745/what-is-the-use-of-cleaned-data-in-django

        print(dir(form)) # Imprimo todos los metodos, funciones y demas cosas tiene form

        print(request.FILES["photo"]) # Lo imprimo para ver que es un diccionario, y accedo a su valor.

        # print(request.FILES["archivo"]) #Esto se lo agregue para probar lo del multicarga de archivos.

        print(request.FILES) # Lo imprimi para ver que es un <MultiValueDict: {'photo': [<InMemoryUploadedFile: photoshop-logo.png (image/png)>]}>

        if form.is_valid():
            print(form.is_valid()) # el is_valid() devuelve un True o False
            form.save()
        return render(request, "app_image/base.html", {"form": form, "images": images})
    
    else:
        form = ImageForm()
        return render(request, "app_image/base.html", {"form": form, "images": images})

def search(request):

    print(request.GET) # Imprime un <QueryDict> con su clave-valor

    query_dict = request.GET # Esto es un diccionario

    print(f'query_dict.get("q") --> {query_dict.get("q")}') # Viene de aca: <input class="form-control me-2" type="search" name="q">

    query = query_dict.get("q")

    ################## Lo tenia de otra forma y lo solucione asi: https://es.stackoverflow.com/questions/53281/django-error-matching-query-does-not-exist

    image_object = None
    mensaje = "" # si no defino mensaje aca, me va a dar el error: ocal variable 'mensaje' referenced before assignment porque mensaje en el contexto no va a existir
    
    if Image.objects.filter(name=query).exists():
        image_object = Image.objects.get(name=query)
    else:
        mensaje = f"No hay resultado para su busqueda {query}"

    ##################################

    print(f"Este es el image_object: {image_object}")
    context = {"image_object": image_object, "mensaje":mensaje}
    return render(request, "app_image/search.html", context)

def contact(request):

    # Cuando envio por metodo POST (o sea aprieto en enviar), guardo en esas variables lo que traigo del html (en la propiedad name="" de cada uno de esos campos).
    # Lo valide desde el front (solo html), pero habria que hacer una validacion con JavaScript y desde aca (backend).
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        template = render_to_string("app_image/email-template.html", {
            'name': name,
            'email': email,
            'message': message,
        })

        email_construct = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ["tinchoz8426@gmail.com"] # le puedo pasar dentro de la lista mas correos: "martinzotti@hotmail.com"
        )

        email_construct.fail_silently = False

        messages.success(request, "Mensaje enviado con exito")
        email_construct.send()

        return redirect("contact")

    return render(request, "app_image/contact.html")

# Vista generica para mostrar un template.
# Hay que mirar desde cero las vistas basadas en clase
# 1- https://docs.hektorprofe.net/django/web-playground/cbv-templateview/
# 2- https://docs.djangoproject.com/en/4.1/ref/class-based-views/
# 3- https://docs.djangoproject.com/en/4.1/topics/class-based-views/
class AboutView(TemplateView):
    template_name = "app_image/about.html"