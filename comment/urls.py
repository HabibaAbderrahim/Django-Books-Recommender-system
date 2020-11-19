from django.urls import path , include
from . import views
from movie import views as vv

app_name = 'comment'
urlpatterns = [
     path('movies/', include('movie.urls', namespace='movies')),
     path('com/', views.post_detail, name='com'),
]