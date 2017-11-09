# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Courses

# Create your views here.


class CourseListView(View):
    def get(self,request):
        all_courses = Courses.objects.all().order_by('-add_time')

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
            'sort':sort

        })


