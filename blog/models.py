from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
	creado = models.DateTimeField(auto_now_add=True, editable=False)
	editado = models.DateTimeField(auto_now_add=True, editable=False)
	titulo = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, blank=True, default='')
	contenido = models.TextField()
	publicado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug == slugify(self.title)
		super(Post, self).save(*args, **kwargs)
