from django.test import TestCase

class TestGallery(TestCase):
    def test_gallery_home_urls_exists(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
