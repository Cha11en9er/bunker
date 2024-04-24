from django.db import models

class user(models.Model):
    login = models.TextField()
    email = models.TextField()
    password = models.TextField()