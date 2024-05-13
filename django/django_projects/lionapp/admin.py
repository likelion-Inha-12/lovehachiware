from django.contrib import admin
from .models import Post,Comment
# Register your models here.

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)  # 사이트에서 admin으로 얘네를 관리하겠다