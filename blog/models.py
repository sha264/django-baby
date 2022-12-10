from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    releasedate = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    #モデルを文字列で表す
    def __str__(self):
        return self.title