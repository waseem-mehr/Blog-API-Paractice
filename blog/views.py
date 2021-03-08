from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from rest_framework import generics
from .models import Post,PostCategorey
from .serializers import PostSerializer
# Create your views here.

class HomePage(generic.TemplateView):
    template_name="home.html"


class PostList(generics.ListCreateAPIView):
    queryset=Post.post_publish_objects.all()
    serializer_class=PostSerializer
    

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    pass
