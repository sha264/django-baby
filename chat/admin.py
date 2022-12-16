from django.contrib import admin

# Register your models here.
from .models import Account, Chat, Group

class AccountChatInline(admin.TabularInline):
    model = Chat
    extra = 1


class GroupChatInline(admin.TabularInline):
    model = Chat


class AccountAdmin(admin.ModelAdmin):
    inlines = [AccountChatInline]

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupChatInline]

admin.site.register(Account, AccountAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Chat)