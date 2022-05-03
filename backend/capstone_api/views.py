from django.http import QueryDict
from rest_framework import generics 
from capstone.models import Post #from the path import the models Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset= Post.posotobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer