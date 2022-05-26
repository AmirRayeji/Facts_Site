from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from theory.models import Post


class PostTest(TestCase):
    @classmethod
    
    def setUpTestData(cls):
        cls.user= User.objects.create(username='user1')
        cls.post1= Post.objects.create(
            title='Post1',
            text='This is the description of Post1',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.post2= Post.objects.create(
            title='Post2',
            text='Lorem ipsum post2',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
        )


    def test_post_model_string(self):
        post=self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'Post1')
        self.assertEqual(self.post1.text, 'This is the description of Post1')

    def test_post_list_url(self):
        response= self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_theory_list_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response= self.client.get(f'/detail/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_theory_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
