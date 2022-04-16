from django.urls import include, path
from core.views import ping_pong


urlpatterns = [
    path('ping/', ping_pong) #, name='ping_pong_url'),
]