from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_group = models.ManyToManyField('Group',through='Chat',blank=True, null=True,related_name='group_user_set')

    def __str__(self):
        return self.username

class Chat(models.Model):
    content = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Chats')
    group = models.ForeignKey('Group',on_delete=models.CASCADE,related_name='Chats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Group(models.Model):
    groupname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    account_group = models.ManyToManyField(Account, through='Chat',related_name='user_group_set')

    def __str__(self):
        return self.groupname
