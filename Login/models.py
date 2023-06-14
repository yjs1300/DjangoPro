from django.db import models

# Create your models here.
class User(models.Model): # 회원가입에서 입력한 값을 받아오기 위함.
    username = models.CharField(max_length=255, verbose_name='id') # 아이디
    name =  models.CharField(max_length=255, verbose_name='name') # 가입자명
    password = models.CharField(max_length=255, verbose_name="Password") # 비밀번호
    email = models.EmailField(max_length=255) # 이메일 
    registered_dttm = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = "userinfo"