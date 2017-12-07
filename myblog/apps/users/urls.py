# _*_ encoding:utf-8 _*_
from django.conf.urls import url,include

from .views import UserinfoView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),

]

