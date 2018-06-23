from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required
# Create your views here.

# def home(request):
#     return HttpResponse('<h1>home</h1>')

def user_login(request):
    msg=None
    if request.method=='GET':
        return render(request,"user/login.html")
    elif request.method =="POST":
        data =request.POST
        username =data.get('username')
        print(username)
        password =data.get('password')
        print(password)

        user= authenticate(username=username,password=password)
        if user is not None:
            print('is_authenticated:', user.is_authenticated)
            login(request,user)
            # return HttpResponse('登录成功')
            # return redirect('/task/list/')  # 极其重要!!!!!!!!!
            return redirect(reverse('userlist'))  # 极其重要!!!!!!!!!
        msg='用户名或密码错误'
        return render(request,'user/login.html',{'msg':msg})
        return HttpResponse('登录失败')

        # return HttpResponse(data)

def user_logout(request):
    logout(request)
    # return redirect('task')
    return redirect(reverse('one'))   # 尝试 反向解析 使用的'one'

def home(request):
    return render(request,'user/home.html')

@login_required
def create(request):
    return  HttpResponse('这是创建页面')
