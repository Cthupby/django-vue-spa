from django.contrib import admin
from core.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'amount', 'distance')
    search_fields = ['title', 'distance']

