from django.contrib import admin
from . models import User 

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "name","email") # 관리할 컬럼을 지정함.
    
admin.site.register(User, UserAdmin)
