from django.test import TestCase
from blog.models import Blog

class TestModel(TestCase):
    def setUp(self):
        self.project = Blog.objects.create(
            title = 'Python trees',
            author = 'Bob',
            rubric = 'Algorithms',
            body = 'This is..',
            time = '123'
        )

    
