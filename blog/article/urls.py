from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.article_list),#路由规则
    url(r'^(\d+)$',views.article_detail),
]