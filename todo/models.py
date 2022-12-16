from django.db import models
#モデルを作成->データベースに保存
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author=models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True,related_name='todos')
    completed = models.BooleanField(default=False)
    duedate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    #モデルを文字列で表す
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    todos = models.ManyToManyField(Todo, related_name="tags")

    def __str__(self):
        return self.name