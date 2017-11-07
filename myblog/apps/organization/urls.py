# _*_ encoding:utf-8 _*_
from django.conf.urls import url,include

from .views import OrgView,AddUserAskView,OrgHomeView


urlpatterns = [
    # 课程机构部分
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    # 我要咨询
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    # 机构首页
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
]

