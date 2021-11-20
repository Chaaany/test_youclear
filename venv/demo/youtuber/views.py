from django.shortcuts import render
from .models import *
from django.urls import reverse
# 비밀번호 재설정 후 리다이렉트 페이지 커스텀
from allauth.account.views import PasswordChangeView


# Create your views here.
def index(request):
    # 로그인 여부 출력
    # print(request.user.is_authenticated)
    
    return render(request, "youtuber/index.html")

def detail(request, page_id):
    youtuber = DetailModel.objects.get(id=page_id)
    
    context = {
        'youtuber': youtuber
    }
    return render(request, 'youtuber/detail.html', context)

# 기존 비밀번호 변경 뷰 오버라이딩 - 상속받아서 작동방식 바꿔주는 것
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")