from django.db import models

# Create your models here.
class City(models.Model):
    title=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.title