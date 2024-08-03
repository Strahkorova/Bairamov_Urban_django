from django.db import models


# Create your models here.
class MyNewModel(models.Model):
    title = models.CharField(max_length=255)


class MySecondNewModel(models.Model):
    another_title = models.CharField(max_length=255)


class MyNewTableFromPG(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'MyNewTable'
