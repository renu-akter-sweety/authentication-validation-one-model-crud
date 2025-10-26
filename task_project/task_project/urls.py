
from django.contrib import admin
from django.urls import path
from task_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',basepage,name='baseurl'),
    path('taskurl',taskpage,name='taskurl'),
    path('signupurl',sign_up_page,name='signupurl'),
    path('loginurl',loginpage,name="loginurl"),
    path('logouturl',logoutpage,name="logouturl"),
    path('editurl/<int:id>',editpage,name="editurl"),
    path('deleteurl/<int:id>',deletepage,name="deleteurl"),




         
]
