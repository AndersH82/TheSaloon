from django.test import TestCase, Client
from django.urls import reverse, resolve
from the_saloon.views import home, profile_list, login_user, update_user, upload_image
from the_saloon.models import Profile, User

# Test Urls

class TestUrls(TestCase):

    def test_list_url_is_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)


    def test_creat_url_is_resolves(self):
        url = reverse('profile_list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile_list)
    

    def test_login_url_is_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, login_user)


    def test_update_user_url_is_resolves(self):
        url = reverse('update_user')
        print(resolve(url))
        self.assertEqual(resolve(url).func, update_user)


    def test_upload_image_url_is_resolves(self):
        url = reverse('upload_image')
        print(resolve(url))
        self.assertEqual(resolve(url).func, upload_image)

# Test Views


class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user_id=pk', password='password')

    def test_profile_view(self):
        self.client.login(username='user_id=pk', password='password')

        response = self.client.get('/profile/')
    
    def test_profile_views_requires_login(self):

        response = self.client.get('/login/')


class LoginUserTest(TestCase):

    def test_login_success(self):
        response = self.client.post(reverse('login'), {'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url == reverse('login'))

    def test_login_fail(self):
        response = self.client.post(reverse('login'), {'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url == reverse('login'))

    def test_login_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

# Test Models

class 