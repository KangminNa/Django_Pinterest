from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 정책부분을 담당, 객체가 사라질때 어떻게 할 것인지. 프로필도 같이 없어지게 설정(다른 여러가지 방법이 있음)
    # related_name : request.user 따로 profile 유저를 찾지 않아도 이름을 정해주기.
    # nickname = models.CharField() -> request.user.profile.nickname 이렇게 불러올 수 있음
    image = models.ImageField(upload_to='profile/', null=True) # 이미지 필드 생성
    nickname = models.CharField(max_length=20, unique=True, null=True) # 닉네임 유일하게 설정하기
    message = models.CharField(max_length=100, null=True) # 한줄소개

