from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class ShortyURLsTest(TestCase):
    def test_index_page(self):
        url = reverse("home")
        self.assertEqual(url, "/")

    def test_api_page(self):
        url = reverse("api")
        self.assertEqual(url, "/api/")

    def test_api_shorten_page(self):
        url = reverse("shortener", kwargs={"shortcode": "9L_kQ2"})
        self.assertEqual(url, "/api/shorten/9L_kQ2")

    def test_api_stats_page(self):
        url = reverse("stats", kwargs={"shortcode": "9L_kQ2"})
        self.assertEqual(url, "/api/stats/9L_kQ2")

    def test_redirect_page(self):
        url = reverse("redirect", kwargs={"shortened_path": "9L_kQ2"})
        self.assertEqual(url, "/9L_kQ2")
