from django.test import TestCase
from .models import Image, Profile, Comments

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.new_image = Image(image="image", image_name="john", image_caption="Amazing", likes=1, comments="comment", profile="Profile")
        self.new_image.save_image()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))


class TestProfile(TestCase):
    def setUp(self):
        pass
class TestComments(TestCase):
    def setUp(self):
        pass



