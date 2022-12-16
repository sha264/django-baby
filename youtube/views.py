from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Account, Video, Comment, Like


#あるAccountが出したVideo一覧
class AccountVideoView(APIView):
    def get(self, request, account_id):
        videos = Video.objects.filter(account_id=account_id)
        res_videos = []
        for video in videos:
            res_video = {
                'id': video.id,
                'title': video.title,
                'description': video.description,
                'video': video.video.url,
                'thumbnail': video.thumbnail.url,
                'created_at': video.created_at,
                'updated_at': video.updated_at,
                'account': video.account.username,
                'comment_accounts': video.comment_accounts.all().values('username'),
                'like_accounts': video.like_accounts.all().values('username'),
            }
            res_videos.append(res_video)
        return Response(res_videos)

class VideoCommentView(APIView):
    def get(self, request, video_id):
        comments = Comment.objects.filter(video_id=video_id)
        res_users = []
        for comment in comments:
            res_user = {
                'username': comment.account.username,
            }
            res_users.append(res_user)
        return Response(res_users)