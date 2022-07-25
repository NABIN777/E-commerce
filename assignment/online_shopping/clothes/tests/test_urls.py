from django.test import TestCase, Client
from django.urls import reverse,resolve
from clothes.views import *


class UrlsTest(TestCase):
    def test_homeurlisresolved(self):
        url=reverse('clothes:homepage')
        self.assertEqual(resolve(url).func,homepage)

    def test_showcatisresolved(self):
        url=reverse('clothes:show_categories')
        self.assertEqual(resolve(url).func,show_categories)

    def test_delete_clotheisresolved(self):
        url=reverse('clothes:delete_clothe', args=[2])
        self.assertEqual(resolve(url).func,delete_clothe)




