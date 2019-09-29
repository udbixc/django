"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#导包
from App import views

#定义路由，配置App的view的函数，hello就是定义的函数
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', views.hello),
    url(r'^lala/', views.lala),
    url(r'^index/', views.index),
    url(r'^addstudent/', views.add_student),
    url(r'^getstudent/', views.get_students),
    url(r'^updatestudent/', views.update_student),
    url(r'^deletestudent/', views.delete_student),
]

#python自带flask的script功能

