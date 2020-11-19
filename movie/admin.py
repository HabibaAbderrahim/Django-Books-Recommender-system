from django.contrib import admin
from .models import Movie 
from .models import Post
from .models import TopBooks , Top

#Movie =Book 
admin.site.register(Movie)
admin.site.register(Post)
admin.site.register(TopBooks)
admin.site.register(Top)
