from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *

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