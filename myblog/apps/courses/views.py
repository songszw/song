# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Courses
from operation.models import UserFavorite

# Create your views here.


class CourseListView(View):
    def get(self,request):
        all_courses = Courses.objects.all().order_by('-add_time')

        hot_courses = Courses.objects.all().order_by('-click_nums')[:3]

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by('-students')
            elif sort == 'hot':
                all_courses = all_courses.order_by('-click_nums')

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses,6, request=request)
        courses = p.page(page)

        return render(request,'course-list.html',{
            'all_courses':courses,
            'sort':sort,
            'hot_courses':hot_courses
        })


class CourseDetailView(View):
    # 课程详情页
    def get(self,request,course_id):
        course = Courses.objects.get(id=int(course_id))
        # 增加课程点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user = request.user,fav_id=course.id,fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user = request.user,fav_id=course.course_org.id,fav_type=2):
                has_fav_org = True


        tag = course.tag
        if tag:
            relate_coures = Courses.objects.filter(tag = tag)[:1]
        else:
            relate_coures = []


        return render(request,'course-detail.html',{
            'course':course,
            'relate_coures':relate_coures,
            'has_fav_course':has_fav_course,
            'has_fav_org':has_fav_org
        })


class CourseInfoView(View):

    def get(self,request,course_id):
        course = Courses.objects.get(id = int(course_id))
        return render(request,'course-video.html',{
            'course':course
        })
