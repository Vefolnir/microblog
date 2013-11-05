from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = "creado"
	fields = ("publicado", "titulo", "contenido")
	list_display = ["publicado", "titulo", "editado"]
	list_display_links = ["titulo"]
	list_editable = ["publicado"]
	list_filter =["publicado", "editado"]



admin.site.register(Post, PostAdmin)

