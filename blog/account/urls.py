from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^login/$',views.user_login),
    url(r'^login_handler/$',views.login_handler),
    url(r'^user_logout/$',views.user_logout),
]