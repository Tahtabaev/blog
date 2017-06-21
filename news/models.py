from django.db import models

class Newclients(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=124)
