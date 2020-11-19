
from django.urls import path , include
from . import views
from movie import views as vv

app_name = 'login'
urlpatterns = [
     path('', views.send_email, name='send_email'),
     path('session/', views.user_login, name='user_login'),
     path('success/', views.user_success, name='user_success'),
     path('sessionout/', views.user_logout, name='user_logout'),
     path('movies/', include('movie.urls', namespace='movies')),
     path('login/', views.login_page, name='login'),
     path('logout/', views.logout_page, name='logout'),
]