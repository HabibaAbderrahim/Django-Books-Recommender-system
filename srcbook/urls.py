
from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from login import views as v 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movie.urls', namespace='movies')),
    path('login/', include('login.urls', namespace='login')),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
