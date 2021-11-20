# 로그인 구현
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DetailModel, User

# Register your models here.
# 유투버 상세페이지 구현
admin.site.register(DetailModel)

# 로그인 구현 - 유저모델 등록
admin.site.register(User, UserAdmin) 
# 커스텀 필드 관리자 페이지 출력 - 커스텀 필드는 관리자 기본 페이지에 출력 X
UserAdmin.fieldsets += (("custom fields", {"fields": ("nickname",)}),)
