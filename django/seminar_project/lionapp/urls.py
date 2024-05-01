from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_post),
    path('<int:pk>/',views.get_post),
    path('delete/<int:pk>',views.delete_post),
    path('comments/<int:post_id>',views.get_comment), # 주소뒤에 붙을 이름/pk값,views에 선언한 함수명
    path('like_post/<int:post_id>',views.likke_post),
    path('likecount_post/<int:post_id>',views.likecount_post),
    path('list_post_by_comment/<int:post_id>',views.list_post_by_comment)
]