from . import views
from django.urls import path

urlpatterns=[
path('',views.index,name='index'),
path('fileupload',views.fileupload,name='fileupload'),
path('setcookie',views.setcookie,name='setcookie'),
path('getcookie',views.getcookie,name='getcookie'),
path('home',views.index,name='index'),
path('ajaxload',views.ajaxload,name='ajaxload'),
path('ajaxdata',views.ajaxdata,name='ajaxdata'),
path('viewcontact',views.viewcontact,name='viewcontact'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('logincode',views.logincode,name='logincode'),
path('dashboard',views.dashboard,name='dashboard'),
path('dashcode',views.dashcode,name='dashcode'),
path('about',views.about,name='about'),
path('service',views.service,name='service'),
path('contact',views.contact,name='contact'),
path('Editcontact',views.Editcontact,name='Editcontact'),
path('edit',views.edit,name='edit'),
path('Deletecontact',views.Deletecontact,name='Deletecontact'),
path('contactcode',views.contactcode,name='contactcode'),
path('gallery',views.gallery,name='gallery')
]
