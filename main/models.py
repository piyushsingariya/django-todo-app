# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)