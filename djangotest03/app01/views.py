from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
# Create your views here.

USER_DICT = {
   '1':{'name':'aelx1','email':'aelx@1231.com'},
   '2':{'name':'aelx2','email':'aelx@1232.com'},
   '3':{'name':'aelx3','email':'aelx@1233.com'},
   '4':{'name':'aelx4','email':'aelx@1234.com'},
   '5':{'name':'aelx5','email':'aelx@1235.com'},
}

def index(request):
    return render(request,'index.html',{'user_dict':USER_DICT})

def detail(request,nid):
    # nid = request.GET.get('nid')
    # return HttpResponse(nid)
    dict_info = USER_DICT[nid]
    return render(request,'detail.html',{'dict_info':dict_info})
    # detail_info = USER_DICT[nid]
    # return render(request,'detail.html',{'detail_info':detail_info})
'''
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username == 'song' and password == '123':
            return redirect('index.html')
        else:
            return render(request, 'login.html')
    else:
        return redirect('index.html')


    # return redirect('index.html')
    # print(request.method)
    # return render(request, 'login.html')
'''
from django.views import View
from app01 import models
class Login(View):
    def get(self,request):
        print(request.method)

        return render(request, 'login.html')

    def post(self,request):
        print(request.method)
        suer = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        result = models.UserInfo.objects.filter(username=suer)
        for row in result:
            if suer == row.username and pwd == row.password:
                return redirect('index.html')
            else:
                return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        repwd = request.POST.get('repassword')
        if name != None and pwd == repwd:
            models.UserInfo.objects.create(
                username = name,
                password = pwd
            )
        return render(request,'login.html')
    else:
        return redirect('register.html')

