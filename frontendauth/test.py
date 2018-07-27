from django.test import TestCase
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model


class SimpleTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        User = get_user_model()
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/auth/login', follow=True)
        user = User.objects.get(username='temporary')
        self.assertEqual(response.context['user'].email, 'temporary@gmail.com')