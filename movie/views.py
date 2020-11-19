from django.shortcuts import render , get_object_or_404

from django.views.generic import ListView , DetailView
from django.http.request import  HttpRequest

from django.views.generic.dates import YearArchiveView

from .models import Movie  ,  TopBooks , Post , Top
from .forms import CommentForm
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login

from django.http.response import HttpResponse, HttpResponseBadRequest


class MovieList (ListView):
    model = Movie 
    paginate_by = 1
    


class MovieDetail (DetailView):
    model = Movie 
    
    def get_object(self):
        object = super(MovieDetail , self).get_object()
        object.count += 1
        object.save()
        return object
    
    

    def get_context_data(self , **kwargs) :
        context = super(MovieDetail , self).get_context_data(**kwargs)
        context['tops'] =Top.objects.filter(book=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        
       
        print(context)
        return context
    


      
class MovieCategory (ListView):
    model = Movie 
    paginate_by = 1

    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category= self.category )
        return movies

    def get_context_data(self , **kwargs):
        context = super(MovieCategory , self).get_context_data(**kwargs)
        context ['movie_category'] = self.category
        return context

class MovieLanguage (ListView):
    model = Movie 
    paginate_by = 1

    def get_queryset(self):
        self.language = self.kwargs['language']
        movies = Movie.objects.filter(language= self.language )
        return movies

    def get_context_data(self , **kwargs):
        context = super(MovieLanguage , self).get_context_data(**kwargs)
        context ['movie_language'] = self.language
        return context

class MovieSearch (ListView):
    
    model = Movie 
    paginate_by = 1
   
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
           object_list = self.model.objects.filter(title__icontains=query )
          
        else:
            object_list = self.model.objects.none()
        return object_list





