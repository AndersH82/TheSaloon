from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from the_saloon.views import home, profile_list, login_user, update_user
from the_saloon.views import upload_image
from the_saloon.models import Shout
from .forms import ProfilePicForm, SignUpForm

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
        self.user = User.objects.create_user(
            username='user_id=pk', password='password')

    def test_profile_view(self):
        self.client.login(username='user_id=pk', password='password')


class LoginUserTest(TestCase):

    def test_login_success(self):
        response = self.client.post(
            reverse('login'), {'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url == reverse('login'))

    def test_login_fail(self):
        response = self.client.post(
            reverse('login'), {'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url == reverse('login'))

    def test_login_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

# Test Models


class ShoutModelTest(TestCase):

    def setUpTestData():
        test_user = User.objects.create_user(
            username="User", password='password')
        Shout.objects.create(user=test_user, body='Test shout body')

    def test_number_of_likes(self):
        shout = Shout.objects.get(id=1)
        self.assertEqual(shout.number_of_likes(), 0)

# Test Forms


class ProfilePicFormTest(TestCase):

    def test_form_fields(self):
        form = ProfilePicForm()
        self.assertSequenceEqual(list(form.fields.keys()), [
                                 'profile_image', 'profile_bio',
                                 'facebook_link', 'instagram_link',
                                 'linkedin_link', 'youtube_link', 'x_link'])

    def test_form_rendering(self):

        form = ProfilePicForm()
        rendered = form.as_p()
        self.assertIn('Profile Picture', rendered)
        self.assertIn('Profile Info', rendered)
        self.assertIn('Facebook Link', rendered)
        self.assertIn('Instagram Link', rendered)
        self.assertIn('Linkedin Link', rendered)
        self.assertIn('Youtube Link', rendered)
        self.assertIn('X Link', rendered)


class ShoutFormTest(TestCase):

    def setUp(self):
        self.shout = Shout.objects.create(body="This is a test shout")

    def tearDown(self):
        Shout.objects.all().delete()


class SignUpFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('register')

    def test_form_initialization(self):
        form = SignUpForm()
        self.assertEqual(len(form.fields),  6)
        self.assertTrue('username' in form.fields)
        self.assertTrue('first_name' in form.fields)
        self.assertTrue('last_name' in form.fields)
        self.assertTrue('email' in form.fields)
        self.assertTrue('password1' in form.fields)
        self.assertTrue('password2' in form.fields)

    def test_form_validation(self):
        form = SignUpForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid_email',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertFalse(form.is_valid())
