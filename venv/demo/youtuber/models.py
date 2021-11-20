from django.db import models
# 태그기능 구현
from taggit.managers import TaggableManager
# 로그인 기능 구현
from django.contrib.auth.models import AbstractUser
# validatior 추가
from .validators import *

# Create your models here.
class DetailModel(models.Model):
    profile = models.ImageField(upload_to="profile/")
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
#    추후 taggit 이용 or view 로직 적용 (, or 띄어쓰기 기준 태그)
    tags = TaggableManager(blank=False)
# 영상 5개까지 추가 가능
    video_1 = models.CharField(max_length=50, blank=False)
    video_2 = models.CharField(max_length=50, blank=True)
    video_3 = models.CharField(max_length=50, blank=True)
    video_4 = models.CharField(max_length=50, blank=True)
    video_5 = models.CharField(max_length=50, blank=True)

    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"유투버 : {self.name}"


# 로그인 기능 구현용
class User(AbstractUser):
    # 닉네임 필드 설정 - unique = True : 중복값 X / migrate을 위해 null = True 설정(초기값설정)
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        # 에러코드 커스텀
        error_messages={'unique' : '이미 사용중인 닉네임입니다.'}
    
    )
# # 이메일 로그인 시 기존 str메소드 오버라이딩
#     def __str__(self):
#         return self.email