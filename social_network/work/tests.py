from django.test import TestCase
from .models import *
from django.urls import reverse
from django.utils import timezone

class SocialTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(login = 'pidoras', password = 'xyesos228', image='fdgdgddg', email = 'pidor@pidor.ru')
        self.theme = Theme.objects.create(name = 'Для гандонов')
        self.theme2 = Theme.objects.create(name = 'Для чётких')
        self.post = Post.objects.create(title='fogokfgf',
    text='gfgdfggg',
    image='fgfdfh',
    date='2024-06-04',
    posted_by=self.user,
    theme=self.theme,
    reaction=0)
        self.post2 = Post.objects.create(title='blyat',
    text='xyi',
    image='fgfdfh',
    date='2024-06-04',
    posted_by=self.user,
    theme=self.theme2,
    reaction=0)
    
    def test_search_user(self):
        data = {'user': self.user.login}
        response = self.client.get(reverse('user-search-user'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user.login, response.content.decode())
        
    def test_search_post(self):
        data = {'post': self.post.title}
        response = self.client.get(reverse('post-search-post'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.post.title, response.content.decode())
        
    def test_search_by_theme(self):
        data = {'id': self.theme.pk}
        response = self.client.get(reverse('post-search-by-theme'), data)
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(self.post.title in response.content.decode())
        
    def test_like(self):
        data = {'id': self.post.pk}
        response = self.client.get(reverse('post-like'), data)
        updated_post = Post.objects.get(pk = self.post.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_post.reaction, 1)
        
    def test_dislike(self):
        data = {'id': self.post.pk}
        response = self.client.get(reverse('post-dislike'), data)
        updated_post = Post.objects.get(pk = self.post.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_post.reaction, -1)


# Create your tests here.
