from django.db import models

# Create your models here.

class submission(models.Model):
	f = models.FileField()
	name = models.CharField(max_length=500, default='')
