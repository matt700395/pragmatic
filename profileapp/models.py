from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') #CASCADE : 유저가 사라지면 그 프로필도 사라지게!
    
    image = models.ImageField(upload_to='profile/', null=True) #프로필 이미지 서버에 저장 : 안 넣어도 괜찮다! null!
    nickname = models.CharField(max_length=20, unique=True, null=True)  #닉네임 중복 불가능
    message = models.CharField(max_length=100, null=True)