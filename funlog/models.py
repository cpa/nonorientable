# -*- coding: utf-8 -*-
from django.db import models

class Funfact(models.Model):
    title = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Publié le', auto_now=True)
    author = models.CharField(max_length=100)
    text = models.TextField()
    urltext = models.CharField(max_length=100)
