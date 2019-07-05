from django.contrib import admin
from .models import BlogArticles
# Register your models here.
#Register your models here
#将之前的建立的模型，在admin.py中进行模型的注册
admin.site.register(BlogArticles)
