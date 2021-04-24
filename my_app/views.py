from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post


# Create your views here.
def index(request):
    return HttpResponse("Yaayyyyy!")


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
