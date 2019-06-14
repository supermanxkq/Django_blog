from django.contrib import admin
from blog.models import Blog
# Register your models here.


#在admin.py文件中注册数据库表，使其在管理页面中显示
admin.site.register(Blog)
