from django.db import models
#モデルを作成->データベースに保存
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    duedate = models.DateTimeField(blank=True, null=True)
    #モデルを文字列で表す
    def __str__(self):
        return self.title