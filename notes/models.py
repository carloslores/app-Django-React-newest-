# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title