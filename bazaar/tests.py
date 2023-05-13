from django.test import TestCase
from django.urls import reverse

class FooterTestCase(TestCase):
    def test_footer_links(self):
        # Test if footer links are working correctly
        response = self.client.get(reverse('terms_and_conditions'))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(reverse('privacy_policy'))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        
    def test_footer_text(self):
        # Test if footer displays correct text
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Online Grocery Shop 2023')
        
    def test_footer_styling(self):
        # Test if footer has correct styling
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'style="color:#ffffff;"')
