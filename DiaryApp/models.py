from django.db import models
from django.forms import DateTimeField
from django.conf import settings

# Create your models here.

class Diary(models.Model):
    id = models.AutoField(primary_key=True) # pk
    title = models.CharField(max_length = 50) # 제목
    content = models.TextField() #내용
    hashTag = models.CharField(max_length = 20) #해시태그
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE) #작성자 
    created_at = models.DateTimeField(auto_now=True) #생성일자
    
    def __str__(self):
        return self.title