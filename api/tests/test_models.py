from django.test import TestCase
from datetime import datetime

from core.models import Post


class PostTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Post.objects.create(date = datetime.today(),
                            title = "South",
                            amount = 12,
                            distance = 859,
                            )

    def test_title(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_date(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'date')

    def test_title_max_length(self):
        post=Post.objects.get(id=1)
        max_length = author._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
