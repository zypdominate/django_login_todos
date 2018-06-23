from django.shortcuts import render,redirect
from django.http import HttpResponse
from task.models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'task/home.html')


@login_required
def create(request):
    if request.method =='GET':
        return render(request,'task/create.html')
    elif request.method =='POST':
        text = request.POST.get('title')

        task = Task(text=text,creator=request.user)  # 很重要的一点, creator =request.user

        # 创建模型的时候,创建了两个参数:text,creator,
        task.save()
        return redirect(list)

@login_required
def list(request):
    user=request.user
    login(request,user)
    tasks = Task.objects.all().filter(completed=True).filter(creator=user)
    # tasks_two = Task.objects.get(completed=False)
    tasks_two = Task.objects.all().filter(completed=False).filter(creator=user)

    # return render(request,"task/list.html",context={"todos":tasks})
    return render(request, "task/create_and_list.html", context={"todos":tasks,"todos_two":tasks_two})
    # return HttpResponse("todo list.")


def todo_update(request,pk):
    task =Task.objects.get(pk=pk)
    task.completed=not task.completed
    task.save()
    return redirect(list)
    # return HttpResponse(task.completed)

def todo_logout(request):
    logout(request)
    return redirect(home)

def todo_delete(request,pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    return redirect(list)
    # return HttpResponse('todo delete')

