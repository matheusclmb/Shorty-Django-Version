from django.test import TestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .models import Shortener


# Create your tests here.
class ShortyURLsTest(TestCase):
    def test_index_page(self):
        url = reverse("home")
        self.assertEqual(url, "/")

    def test_index_false(self):
        url = reverse("home")
        self.assertNotEqual(url, "/api/")

    def test_api_page(self):
        url = reverse("api")
        self.assertEqual(url, "/api/")

    def test_api_false(self):
        url = reverse("api")
        self.assertNotEqual(url, "/")

    def test_api_shorten_page(self):
        url = reverse("shortener", kwargs={"shortcode": "9L_kQ2"})
        self.assertEqual(url, "/api/shorten/9L_kQ2")

    def test_api_shorten_page_false(self):
        url = reverse("shortener", kwargs={"shortcode": "9L_kQ2"})
        self.assertNotEqual(url, "/shorten/9L_kQ2")

    def test_api_stats_page(self):
        url = reverse("stats", kwargs={"shortcode": "9L_kQ2"})
        self.assertEqual(url, "/api/stats/9L_kQ2")

    def test_api_stats_page_false(self):
        url = reverse("stats", kwargs={"shortcode": "9L_kQ2"})
        self.assertNotEqual(url, "/stats/9L_kQ2")

    def test_redirect_page(self):
        url = reverse("redirect", kwargs={"shortened_path": "9L_kQ2"})
        self.assertEqual(url, "/9L_kQ2")

    def test_redirect_page_false(self):
        url = reverse("redirect", kwargs={"shortened_path": "9L_kQ2"})
        self.assertNotEqual(url, "/abc123")

    def test_manual_shortener(self):
        Shortener.objects.create(url="https://www.google.com", shortcode="abc123")
        url = reverse("redirect", kwargs={"shortened_path": "abc123"})
        self.assertEqual(url, "/abc123")

    def test_manual_shortener_false(self):
        Shortener.objects.create(url="https://www.google.com", shortcode="abc123")
        url = reverse("redirect", kwargs={"shortened_path": "abc123"})
        self.assertEqual(url, "/abc123")


class SeleniumTest(TestCase):
    def test_shortener_function(self):
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000")
        input = driver.find_element_by_id("id_url")
        input.click()
        input.clear()
        input.send_keys("https://www.reddit.com")
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "newurl")))
        assert "Your shortened URL is:" in driver.page_source
        driver.close()

    def test_shortener_redirect(self):
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000")
        input = driver.find_element_by_id("id_url")
        input.click()
        input.clear()
        input.send_keys("https://www.reddit.com")
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "newurl")))
        short_url = driver.find_element_by_id("newurl")
        short_url.click()
        driver.switch_to.window(driver.window_handles[1])
        wait_new = WebDriverWait(driver, 10)
        wait_new.until(
            EC.presence_of_element_located((By.CLASS_NAME, "_30BbATRhFv3V83DHNDjJAO"))
        )
        assert "reddit" in driver.page_source
        driver.quit()

    def test_api(self):
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000/api/stats/9L_kQ2")
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[4]')
            )
        )
        driver.switch_to.new_window("tab")
        driver.get("http://127.0.0.1:8000/api/shorten/9L_kQ2")
        assert "shortcode" in driver.page_source
        driver.quit()
