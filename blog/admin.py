from django.contrib import admin
from .models import Post

# Nombre djangogirls/blog/admin.py

#Registra nuestro objeto Post en el administrador
#de django para poder consultar o actuliza informacion
#del o de los Post's
admin.site.register(Post)
