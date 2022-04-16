from rest_framework import generics
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post


def ping_pong(request):
    return JsonResponse('Pong!', safe=False)


class PostList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all posts
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()
