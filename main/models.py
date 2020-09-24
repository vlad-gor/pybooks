from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    publisher = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
        return "{} / {}".format(self.author,self.title)