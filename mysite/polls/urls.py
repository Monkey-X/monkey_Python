from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),#参数name，为URL取名，可以在Django任意地方唯一的引用他，修改一个文件就能全局地修改某个url模式
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vate'),
]