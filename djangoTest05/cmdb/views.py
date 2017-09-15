from django.shortcuts import render,HttpResponse,redirect
from cmdb import models
import json
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    v = models.Busniess.objects.all()
    v1 = models.Busniess.objects.all().values('id','caption')
    return render(request,'index.html',{'v':v,'v1':v1})

def host(request):
    if request.method == 'GET':
        v = models.Host.objects.filter(nid__gt=0)
        v1 = models.Busniess.objects.all()
        return render(request,'host.html',{'v':v,'v1':v1})
    elif request.method == 'POST':
        h = request.POST.get('hostname')
        ip = request.POST.get('ip')
        p = request.POST.get('port')
        c = request.POST.get('code')
        models.Host.objects.create(
            hostname = h,
            ip = ip,
            port = p,
            b_id = c
        )
        return redirect('/cmdb/host')

def host_ajax(request):
    res = {'status':True,'error':None,'data':None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if len(h)>=5:
            models.Host.objects.create(
                hostname=h,
                ip=i,
                port = p,
                b_id = b
            )
        else:
            res['status'] = False
            res['error'] = '太短了'

    except Exception as e:
        res['status'] = False
        res['error'] = '请求错误，错误代码'

    return HttpResponse(json.dumps(res))

# def host_ajax(request):
#     h = request.POST.get('hostname')
#     i = request.POST.get('ip')
#     p = request.POST.get('port')
#     b = request.POST.get('b_id')
#     if len(h)>=5:
#         models.Host.objects.create(
#             hostname=h,
#             ip=i,
#             port = p,
#             b_id = b
#         )
#         return HttpResponse('ok')
#     else:
#         return HttpResponse('the hostname is to short')
#

# def host_ajax(request):
#     h = request.POST.get('hostname')
#     i = request.POST.get('ip')
#     p = request.POST.get('port')
#     b = request.POST.get('b_id')
#     print(h,i,p,b)
#     if len(h)>=5:
#         models.Host.objects.create(
#             hostname=h,
#             ip=i,
#             port=p,
#             b_id=b
#         )
#         return HttpResponse('ok')
#     else:
#         return HttpResponse('the host name is to short')

def app(request):
    if request.method == 'GET':
        app_list = models.Application.objects.all()
        host_list = models.Host.objects.all()
        return render(request,'app.html',{'app_list':app_list,'host_list':host_list})
    # elif request.method == 'POST':
    #     c = request.POST.get('cityname')
    #     i = request.POST.getlist('ips')
    #     return HttpResponse('a')

def addapp(request):
    if request.method=='POST':
        res = {
            'status':True,
            'error':None,
            'data':None
        }
        c = request.POST.get('cityname')
        i = request.POST.getlist('ips')
        obj = models.Application.objects.create(name=c)
        obj.r.add(*i)
        return HttpResponse(json.dumps(res))

def editapp(request):
    if request.method=='POST':
        res = {
            'status': True,
            'error': None,
            'data': None
        }
        c = request.POST.get('cityname')
        i = request.POST.getlist('ips')
        cid = request.POST.get('cid')
        print(c,i,cid)
        obj = models.Application.objects.get(id=cid)
        obj.name = c
        obj.save()
        obj.r.set(i)
        # print(obj.r)
        # obj.r.set(i)
        return HttpResponse(json.dumps(res))


List = []
for i in range(102):
    List.append(i)

def user_list(request):
    getPage = request.GET.get('p',1)
    getPage = int(getPage)
    pageNum,y = divmod(len(List),7)
    startPage = (getPage-1)*7
    endPage = getPage*7
    data = List[startPage:endPage]
    print(pageNum,y)
    if y:
        pageNum+=1
    pages = []
    for i in range(pageNum):
        if i+1 == getPage:
            a = '<a class="bg" href="/cmdb/user_list/?p=%s">%s</a>'%(i+1,i+1)
        else:
            a = '<a href="/cmdb/user_list/?p=%s">%s</a>'%(i+1,i+1)

        pages.append(a)

    pages = ''.join(pages)
    return render(request,'user_list.html',{'data':data,'pages':mark_safe(pages)})

# LIST = []
# for i in range(103):
#     LIST.append(i+1)
# def userList(request):
#     current_page = request.GET.get('p',1)
#     current_page = int(current_page)
#     start = (current_page-1)*10
#     end = current_page*10
#     p = len(LIST)
#     pageNum ,y = divmod(p,10)
#     if y:
#         pageNum+=1
#     pageList = []
#     for i in range(1,pageNum+1):
#         pages = '<a href="/cmdb/user_list/?p=%s">%s</a>' % (i,i)
#         pageList.append(pages)
#
#     str = ''.join(pageList)
#
#     data = LIST[start:end]
#
#     return render(request, 'user_list.html', {'data':data,'str':mark_safe(str)})
user_info = {
    'dachengzi':{'pwd':'123123'},
    'xiaopangzi':{'pwd':"111222"},
}
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method =='POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dic:
            return render(request,'login.html')
        if dic['pwd'] == p:
            res =  redirect('/cmdb/showdtl/')
            res.set_cookie('username001',u)
            return res
        else:
            return render(request,'login.html')

def showdtl(request):
    v = request.COOKIES.get('username001')
    if not v:
        return redirect('/cmdb/login/')
    else:
        return render(request,'showdtl.html',{'v':v})
