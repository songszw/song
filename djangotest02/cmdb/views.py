from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
USER_LIST = [
    {'username':'alex','gender':'男','email':'alex@126.com'},
    {'username':'alisa','gender':'女','email':'alisa@126.com'},
    {'username':'yangzai','gender':'男','email':'yangzai@126.com'},
]


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        gender = request.POST.get('gender',None)
        data = {'username':username,'email':email,'gender':gender}
        USER_LIST.append(data)
    # return HttpResponse('<h1>Hello,world</h1>')
    return render(request,'home.html',{'data':USER_LIST})


def login(request):
    #获取用户提交方法
    # print(request.method)
    error_msg = ''
    if request.method == 'POST':
        #获取用户通过post提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('password',None)
        # print('user:',user,'pwd:',pwd)
        if user == 'root' and pwd == '123456':
            return redirect('/home')
        else:
            error_msg = '用户名或密码错误!'

    return render(request,'login.html',{'error_msg':error_msg})