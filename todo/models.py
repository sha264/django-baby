from django.db import models

# Create your models here.
# todoモデルを作成


class Todo(models.Model):
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=100)
    memo = models.TextField(max_length=100, null=True, blank=True)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
