from django.shortcuts import render

from django.http import HttpResponse

def health(request) :
    return HttpResponse(status = 200, content = "seminar server ok...?") # 200은 정상을 의미하는 상태코드
    # 정상이고, 정상문구로 ~를 출력한다는 뜻임.

# Create your views here.