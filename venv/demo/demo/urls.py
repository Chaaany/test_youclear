"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 이미지 파일 업로드
from django.conf import settings
from django.conf.urls.static import static
# 회원가입 확인 버튼 리다이렉트 페이지
from django.views.generic import TemplateView
# 비밀번호 재설정 리다이렉트 페이지 설정
from youtuber.views import CustomPasswordChangeView

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # youtuber
    path('', include('youtuber.urls')),
    # allauth
    path("email-confirmation-done/", TemplateView.as_view(template_name="youtuber/email_confirmation_done.html"), name="account_email_confirmation_done"),
    # 비밀번호 변경 후 리다이렉트 페이지 설정
    path('password/change/', CustomPasswordChangeView.as_view(), name="account_password_change"),
    path('', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
