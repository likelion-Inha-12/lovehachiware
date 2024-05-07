from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    class Meta:
        model = Post
        fields = ["id","title","content"]
    #serializers.py = 직렬화 파일.
    #Meta class란 , serializers 클래스의 다양한 옵션과 설정 가능.