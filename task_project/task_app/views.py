from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from task_app.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def basepage(req):
    return render(req,'base.html')

def sign_up_page(req):
    if req.method == "POST":
        fullname = req.POST.get('full_name')
        username = req.POST.get('username')
        password = req.POST.get('password')
        user_type=req.POST.get("user_type")
        confirm_password = req.POST.get('confirm_password')
        email = req.POST.get('email')
        username_exists =userinfomodel.objects.filter(username=username).exists()

        if password == confirm_password:

            if username_exists:
                print("username already exists.")
                return redirect("signupurl")
            else:
            
                userinfomodel.objects.create_user(
                    username=username,
                    fullname=fullname,
                    user_type=user_type,
                    email=email,
                    password=confirm_password
                )
                return redirect("loginurl")
        else:
            print("both password are not mtched")

    return render(req, 'sign_up.html')


def loginpage(req):
    if req.method == "POST":
        user_name = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=user_name, password=password)
        print("user: ", user)
        if user:
            login(req, user)
            return redirect("taskurl") 
    return render(req, "log_in.html")

def logoutpage(req):
   logout(req)
   return redirect('loginurl')


@login_required
def taskpage(req):
    task=taskmodel.objects.all()
    user_data=userinfomodel.objects.all()
    if req.method=='POST':
        print("task status: ",req.POST.get('task_status'))
        
        taskmodel.objects.create(
            
        task_name=req.POST.get('task_name'),
        task_description=req.POST.get('task_description'),
        task_status=req.POST.get('task_status'),
        deadline=req.POST.get('deadline'),
        created_by=req.user
        )
        return redirect("taskurl")

    context={
        'task':task,
        'user_data':user_data,

    }
    return render(req,'task.html',context)
@login_required
def editpage(req,id):
    task=taskmodel.objects.get(id=id)
    
    if req.method=='POST':
        
        task.task_name=req.POST.get('task_name')
        task.task_description=req.POST.get('task_description')
        task.task_status=req.POST.get('task_status')
        task.deadline=req.POST.get('deadline')
        task.save()
        return redirect("taskurl")
        
    context={

        'task':task,

    }
    return render(req,'editpage.html',context)
@login_required
def deletepage(req,id):
    taskmodel.objects.get(id=id).delete()
    return redirect("taskurl")
    