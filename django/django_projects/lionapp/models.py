from django.db import models

# Create your models here.
# models 파일 건든 뒤에는 꼭 migration 필수. 변경사항을 쌓아두었다가 마이그레잇 하는것.

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    email = models.EmailField(unique = True) # unique 속성을 가진 email필드 = 데이터베이스에 중복 이메일 허용 안하는 것

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key= True)  #pk인 아이디를 가집니다.
    title = models.CharField(max_length=50) # 50글자가 최대인 문자열
    content = models.TextField(blank = True,null = True) # 본문 작성, 글자 수 제한이 없는 긴 문자열,null과 blank 허용
    create_at = models.DateTimeField(auto_now_add =True) # 처음 Post 생성시, 현재시간 저장 (언제 작성된 필드인지)

    def __str__(self):
        return self.title  #class내에 정의된 이름 항목을 return 시켜야함.


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length = 200)
    post_id = models.ForeignKey(Post, verbose_name = "글", on_delete=models.CASCADE, related_name = "commentss")
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    

class UserPost(models.Model):
    user = models.ForeignKey(Member, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    # user와 post 사이에 관계는 다대다가 아닌, 1:N, M:1 관계로 풀어서 만들어야함.