from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import PostSerializer
from .models import Post


class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['iexact', 'icontains', 'lt', 'gt'],
            'amount': ['iexact', 'icontains', 'lt', 'gt'],
            'distance': ['iexact', 'icontains', 'lt', 'gt'],
        }


class PostList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all posts
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save()
