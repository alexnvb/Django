from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    text = models.TextField()
    date = models.DateField(default=str(datetime.datetime.now())[:10])

    def __str__(self):
        return str(self.id)+" "+str(self.title)