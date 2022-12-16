from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Account,Chat,Group
# Create your views here.

#あるルームのチャット一覧
class GroupChatView(APIView):
    def get(self, request, group_id):
        chats = Chat.objects.filter(group_id=group_id)
        group = Group.objects.get(id=group_id)
        res_chats = []
        for chat in chats:
            res_chat = {
                'username': chat.account.username,
                'content': chat.content,
                'send_at': chat.updated_at,
            }
            res_chats.append(res_chat)
        return Response({
            "groupname": group.groupname,
            "chats": res_chats
        })

#ある人が所属するルーム一覧
class UserGroupView(APIView):
    def get(self, request, account_id):
        user = Account.objects.get(id=account_id)
        groups = user.user_group.all()
        return Response({
            "name": user.username,
            "groups": [group.groupname for group in groups]
        })
        