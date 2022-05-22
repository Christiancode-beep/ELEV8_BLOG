from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('sign',views.sign,name='sign'),
    path('log',views.log,name='log'),
    path('join',views.join,name='join'),
    ]
#     path('content',views.content,name='content'),
#     path('profile',views.profile,name='profile'),
#     path('email',views.email,name='email'),
#     path('my_article',views.my_article,name='my_article'),
# ]