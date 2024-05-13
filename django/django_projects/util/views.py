from django.shortcuts import render
from django.http import HttpResponse
from requests import Response

def health(request) :
    return HttpResponse(status = 200, content = "seminar server ok...?") # 200은 정상을 의미하는 상태코드
    # 정상이고, 정상문구로 ~를 출력한다는 뜻임.
def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)
# Create your views here.