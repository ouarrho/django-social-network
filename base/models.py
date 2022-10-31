from django.db import models

class Post(models.Model):
    description = models.CharField(max_length=200)
