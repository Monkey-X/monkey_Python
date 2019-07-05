from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogArticles(models.Model):
    title=models.CharField(max_length=60) #文章标题
    author=models.ForeignKey(User,on_delete=models.CASCADE,)        #外键，作者
    content=models.TextField()            #文字内容
    pubdate=models.DateTimeField()        #发布时间

    class Meta:
        ordering=("-pubdate",)            #排序 添加排序字段的类型要求是元组，所以要添加逗号

    def __str__(self):
        return self.title