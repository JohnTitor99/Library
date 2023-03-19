from django.test import TestCase, Client
from django.urls import reverse
from .models import Library
import json

# Create your tests here.

class LibraryLibrariesListTests(TestCase):
    def test_libraries_list(self):
        client = Client()

        response = client.get(reverse('libraries'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/main_page.html')