from django.db import models

# Create your models here.
class movies(models.Model):
    name=models.CharField(max_length=250)
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    desc=models.TextField()

    def __str__(self):
        return self.name
