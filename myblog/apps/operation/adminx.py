# _*_ coding:utf-8 _*_
import xadmin

from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse

class UserAskAdmin(object):
    list_display=['name','mobile','course_name','add_time']
    search_fields=['name','mobile','course_name']
    list_filter=['name','mobile','course_name','add_time']


