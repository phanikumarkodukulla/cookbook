from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    requirements = models.TextField()
    procedure = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name