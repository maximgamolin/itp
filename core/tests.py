from django.test import TestCase
from core.models import Post
from django.urls import reverse


class TestHttpOk(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestHttpOk, cls).setUpClass()
        cls.post = Post.objects.create(
            title='foo',
            body='bar'
        )

    def test_homepage(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        response = self.client.get(reverse('post_detail', args=(self.post.id,)))
        self.assertEqual(response.status_code, 200)
