from django.contrib import admin

from .models import Image

# Register your models here.

# Se puede registrar un modelo asi:
# admin.site.register(Image)

# Tambien asi:
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ["id", "photo", "date"]

# O sino asi:
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'date')
    search_fields = ('id', 'photo', 'date')
    # Entiendo que el id y el date (por ser auto_now_add) no aparecen en cada instancia porque no son editables.
    # Podemos poner readonly_fields y ahi si saldran, pero obviamente de solo lectura:
    readonly_fields = ('id', 'date')

admin.site.register(Image, ImageAdmin)