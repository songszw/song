# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg,CityDict
from .forms import UserAskForm
from courses.models import Courses
from operation.models import UserFavorite
# Create your views here.


class OrgView(View):
    # 课程机构列表功能
    def get(self,request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        # 城市
        all_citys = CityDict.objects.all()
        # 筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 类别筛选
        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序
        sort = request.GET.get('sort','')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')
        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs,7, request=request)
        orgs = p.page(page)

        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort
        })


# 我要学习立即咨询
class AddUserAskView(View):
    # 用户添加咨询
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    # 机构首页
    def get(self,request,org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id = int(org_id))
        all_courses = course_org.courses_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page':current_page
        })


class OrgCourseView(View):
    # 机构课程列表页
    def get(self,request,org_id):
        current_page="course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.courses_set.all()
        return render(request,'org-detail-course.html',{
            'all_courses':all_courses,
            'course_org':course_org,
            'current_page':current_page
        })


class OrgDescView(View):
    # 机构课程介绍页
    def get(self,request,org_id):
        current_page="desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request,'org-detail-desc.html',{
            'course_org':course_org,
            'current_page':current_page
        })


class OrgTeacherView(View):
    # 机构讲师
    def get(self,request,org_id):
        current_page="teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()
        return render(request,'org-detail-teachers.html',{
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page':current_page
        })


class AddFavView(View):
    # 用户收藏
    def post(self,request):
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)
        # 首先要判断用户登陆状态
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request,fav_type=fav_type, fav_id=int(fav_id))
        if exist_records:
            # 取消收藏
            exist_records.delete()
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) >0 :
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')
