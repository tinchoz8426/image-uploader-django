from django.urls import path

# from app_image import views --> Otra forma de importar las vistas y despues en el path views.home
from .views import AboutView, contact, home, search

urlpatterns = [
    path('', home, name="index"),
    path('search', search, name="search"),
    path('contact', contact, name="contact"),
    path('about', AboutView.as_view(), name="about"),
]