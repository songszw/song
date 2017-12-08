# _*_ encoding:utf-8 _*_
from django.conf.urls import url,include

from .views import UserinfoView,UploadImageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),
    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

]

