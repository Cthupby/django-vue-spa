from django.urls import include, path
from core.views import ping_pong
from . import views


urlpatterns = [
    path('ping/', ping_pong),
    path('api/posts/', views.PostList.as_view()),
]
