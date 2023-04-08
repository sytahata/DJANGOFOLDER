from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase
from django.urls import reverse
from urllib import response

from .models import Post
#create test for homepage
'''
class homepagetest(SimpleTestCase):
    def test_url_exist_at_correct_location(self): 
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_url_available_by_name(self):
        response=self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    def test_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"home.html")
    def test_template_content(self):
        response=self.client.get("home")
        self.assertContains(response,"<h1>Django Home Page</h1>")

class aboutpagetest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code,200)
    def test_url_available_by_name(self):
        response=self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
        '''

class PostTests(TestCase):
    @classmethod
    def setuptestdata(cls):
        cls.post=Post.objects.create(text="!")
    def test_model_content(self):
        self.assertEqual(self.post.text,"!")
    def test_url_exist_at_correct_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_home_page(self):
        response=self.client.get(reverse("home"))
        #Test URL name for home page
        self.assertEqual(response.status_code,200)
        #Test expected content for homepage template used
        self.assertTemplateUsed(response,"home.html")
        #Test the expected content with this method
        self.assertContains(response,"!")