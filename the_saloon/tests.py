from django.test import TestCase, Client
from django.contrib.auth.models import User
from the_saloon.forms import ShoutForm
from .forms import ProfilePicForm, SignUpForm, UploadImageForm
from .models import Shout, Profile
from django.urls import reverse


# Forms Tests

class TestShoutForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.form_data = {
            'body': 'This is a test shout.',
            'user': self.user.id,
        }

# test the form's validation behavior

    def test_form_validation_with_valid_data(self):
        form = ShoutForm(data={'body': 'This is a test shout.'})
        self.assertTrue(form.is_valid())

# test that it's invalid when the body field is empty

    def test_form_validation_with_empty_body(self):
        form = ShoutForm(data={'body': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'body': ['This field is required.']})

# form validates correctly


class ProfilePicFormTest(TestCase):
    def test_form_validation_empty(self):
        form = ProfilePicForm(data={})
        self.assertTrue(form.is_valid())

# if the form renders correctly

    def test_form_rendering(self):
        form = ProfilePicForm()
        self.assertIn('<input type="file" name="profile_image"', form.as_p())
        self.assertIn('<textarea name="profile_bio"', form.as_p())
        self.assertIn('<input type="text" name="facebook_link"', form.as_p())

# Ensure that the form has the correct fields


class SignUpFormTest(TestCase):
    def test_form_fields(self):
        form = SignUpForm()
        self.assertEqual(
            form.fields['username'].widget.attrs['class'], 'form-control')
        self.assertEqual(
            form.fields['username'].widget.attrs['placeholder'], 'User Name')
        self.assertEqual(
            form.fields['email'].widget.attrs['class'], 'form-control')
        self.assertEqual(
            form.fields['email'].widget.attrs['placeholder'], 'Email Address')

# the form correctly validates input

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
        self.assertEqual(
            form.errors['email'], ['Enter a valid email address.'])

# Ensure that the form's __init__ method correctly sets the attributes

    def test_form_initialization(self):
        form = SignUpForm()
        self.assertEqual(
            form.fields['username'].widget.attrs['class'], 'form-control')
        self.assertEqual(
            form.fields['username'].widget.attrs['placeholder'], 'User Name')

# Upload image test


class UploadImageFormTest(TestCase):
    pass

# Create a form instance with invalid data

    def test_form_with_invalid_data(self):
        form = UploadImageForm(data={'image': ''})
        # Check if the form is not valid
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'image': ['This field is required.']})

# Models Tests


class ShoutModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='testuser')
        Shout.objects.create(
            user=User.objects.get(username='testuser'), body='Test shout')

    def test_number_of_likes(self):
        shout = Shout.objects.get(id=1)
        self.assertEqual(shout.number_of_likes(), 0)

# Test numbers of likes

    def test_number_of_likes_method(self):
        shout = Shout.objects.get(id=1)
        # Assuming you have a user to like the shout
        user = User.objects.create(username='anotheruser')
        shout.likes.add(user)
        self.assertEqual(shout.number_of_likes(), 1)

# Test profile is created successfully with a user


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        # Ensure a profile does not already exist for this user
        Profile.objects.filter(user=self.user).delete()
        self.profile = Profile.objects.create(user=self.user)

    def test_profile_creation(self):
        self.assertIsInstance(self.profile, Profile)
        self.assertEqual(self.profile.__str__(), 'testuser')

    def test_profile_modification(self):
        self.profile.profile_bio = 'This is a test bio.'
        self.profile.save()

        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.profile_bio, 'This is a test bio.')

    def test_get_or_create_profile(self):
        profile, created = Profile.get_or_create_profile('testuser')
        self.assertFalse(created)
        self.assertEqual(profile.user.username, 'testuser')


class ProfileCreationTest(TestCase):
    def setUp(self):
        # Set up any necessary data before each test
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_profile_creation(self):
        # Check if a Profile instance was created
        self.assertIsNotNone(Profile.objects.filter(user=self.user).first())

# Test urls


class LoginUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_login_user_view(self):
        response = self.client.post(
            reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


class HomeURLTest(TestCase):
    def test_home_url_exists_at_desired_location(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 302)


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_home_view_with_login(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

# View test


class ProfileListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.profile, created = Profile.objects.get_or_create(user=self.user)
