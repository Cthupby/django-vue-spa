from django.urls import include, path
from . import views


urlpatterns = [
    path('api/posts/', views.PostList.as_view()),
]
