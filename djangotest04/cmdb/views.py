from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.

def login(request):
    if request.method == 'GET':

        return render(request,'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user',None)
        p = request.POST.get('pwd',None)
        result = models.UserInfo.objects.filter(username=u,password=p)
        if result:
            return redirect('index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request,'login.html')


def index(request):
    return render(request,'index.html')

def userlist(request):

    user_list = models.UserInfo.objects.all()
    return render(request,'userlist.html',{'userlist':user_list})

def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method =='POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        rp = request.POST.get('repwd')
        if p == rp:
            models.UserInfo.objects.create(username = u,password = p)
            return redirect('login.html')

def details(request,nid):
    obj = models.UserInfo.objects.filter(id = nid).first()
    return render(request, 'details.html', {'obj': obj})

def userEdit(request,nid):
    if request.method=='GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'userEdit.html', {'obj': obj})
    elif request.method=='POST':
        aid = request.POST.get('id')
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        print(aid)
        models.UserInfo.objects.filter(id = aid).update(username=u,password=p)
        return redirect('/cmdb/userlist')
    else:
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'userEdit.html', {'obj': obj})

def delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/userlist')
