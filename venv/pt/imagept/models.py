from django.db import models
from django.db.models.fields import CharField
from django.forms.fields import ImageField
from taggit.managers import TaggableManager

# 로그인 기능 구현
from django.contrib.auth.models import AbstractUser

# Create your tests here.
# 1. pip install pillow  -> pillow 패키지 설치
# 2. 
class ImageModel(models.Model):
    name = models.CharField(max_length=15)
    # blank 넣으면 이미지 넣지 않아도 된다는 뜻
    image = models.ImageField(upload_to="profile", blank=False)
    tags = TaggableManager()
    video = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractUser):




# class EmbedModel(models.Model):
#     pass


# class PlaylistModel(models.Model):
#     pass


# class SignModel(models.Model):
#     pass


# class SignupModel(models.Model):
#     pass
