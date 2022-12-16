from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('group/<int:group_id>/chats/', views.GroupChatView.as_view(), name='group_chat'),
    path('account/<int:account_id>/group/', views.UserGroupView.as_view(), name='user_group'),#nameなに
]