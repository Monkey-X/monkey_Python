from django.shortcuts import render
from .models import BlogArticles
# Create your views here.
def article_list(request):#创建的视图函数
    blogs=BlogArticles.objects.all()#Django默认生成的一个管理类，负责和数据库的交互，（ORM）
    return render(request,"article/list.html",{"blogs":blogs})#结合一个给定的模板和一个给定的上下文字典（key-value），返回一个渲染后的HttpResponse对象

def article_detail(request,id):
    article = BlogArticles.objects.get(id=id)
    return render(request,"article/detail.html",{"article":article})