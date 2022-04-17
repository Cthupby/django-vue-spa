from rest_framework import generics
from rest_framework import filters

from .serializers import PostSerializer
from .models import Post


class PostList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all posts
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['date', 'title', 'amount', 'distance']
    ordering_fields = ['date', 'title', 'amount', 'distance']

    def perform_create(self, serializer):
        serializer.save()
