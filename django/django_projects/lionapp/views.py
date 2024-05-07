from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from lovehachiware.django.django_projects.lionapp.serializers import PostSerializer
from .models import *
from rest_framework.response import Response
import json

def create_post (request) :
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title'),
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()
        return JsonResponse({'message':'성공적입니다. 살았어요!'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id' : post.pk,
        '제목' : post.title,
        '내용' : post.content,
        '메시지' : '조회 성공'
    }
    return JsonResponse(data, status=200)

def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" :f"id:{pk} 포스트 삭제 완료 "
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})


def get_comment(request, post_id):   #post에 대한 comment 가져오는 api
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.commentss.all()
        return HttpResponse(comment_list, status=200) #200 - 서버가 요청을 제대로 처리했다는 뜻
    
def api_response(data, message, status):
    response = {
        "message":message,
        "data": data
    }
    return Response(response, status=status) # 앞에 status는 Response의 것, 뒤에는 api_response 것.

@api_view(['POST'])
def create_post_v2(request):
    post = Post(
        title = request.data.get('title'),
        content = request.data.get('content')
    )
    post.save()

    message = f"id: {post.pk}번 포스트 생성 성공이다욧"
    return api_response(data = None,message = message, status = status.HTTP_201_CCREATED)

class PostApiView(APIView):

    def get_object(self, pk): #클래스에서는 self 필수, 여기서 get object를 쓰겠다.
        post = get_object_or_404(Post, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_object(pk)

        postSerializer = PostSerializer(post)  #여기에 넣어주면 객체를 직렬화 과정을 통해 json 형식으로 변경해줌.
        message = f"id: {post.pk}번 포스트 조회 성공"
        return api_response(data = postSerializer.data, message = message, status = status.HTTP_200_OK)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        
        message = f"id: {pk}번 포스트 삭제 성공"
        return api_response(message = message, status = status.HTTP_200_OK)