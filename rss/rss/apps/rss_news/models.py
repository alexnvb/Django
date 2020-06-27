from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    text = models.TextField()

    def __str__(self):
        return str(self.id)+" "+str(self.title)