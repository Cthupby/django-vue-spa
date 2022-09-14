from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'amount', 'distance')
    search_fields = ['title', 'distance']

admin.site.register(PostAdmin)
