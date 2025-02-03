from django.urls import include, path
from core import views


urlpatterns = [
    path('api/posts/', views.PostList.as_view()),
]
