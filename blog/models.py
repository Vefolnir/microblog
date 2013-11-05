# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    editado = models.DateTimeField(auto_now_add=True, editable=False)
    titulo = models.CharField(max_length=255, verbose_name=u'Título')
    slug = models.SlugField(max_length=255, blank=True, default='')
    contenido = models.TextField()
    publicado = models.BooleanField(default=True)
    autor = models.ForeignKey(User, related_name="posts")

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)
