from django.shortcuts import render

#importing http responses
from django.http import HttpResponse

from django.views.generic import TemplateView

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
#setting up home page view
#def homepageview(request):
    #return HttpResponse("Hello Django ")

#create class based view for homepageview
class homepageview(ListView): 
    model=Post
    template_name = "home.html"
#create class based view for aboutpageview
class aboutpageview(TemplateView):
    template_name = "about.html"
class detailview(DetailView):
    model=Post
    template_name="post_details.html"
class createviewpost(CreateView):
    model=Post
    template_name="post_new.html"
    fields=["title","author","body"]
class updateviewpost(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=["title","body"]
class deleteviewpost(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url = reverse_lazy("home")