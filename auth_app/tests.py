from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.authtoken.models import Token

from .models import User



class SignUpTest(APITestCase):
    def test_signUp(self):
        ''' Ensure we can create a new Sign-Up object '''
        url = reverse('sign-up')
        data = {
            "full_name": "Lisa Meier",
            "email": "lisa.meier@example.de",
            "password": "JoinTest2026!",
            "confirm_password": "JoinTest2026!",
            "privacy_policy": True
        }
        
        email = data['email']
        
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"full_name": "Lisa Meier", "email": "lisa.meier@example.de"}) #Verifies that the response contains exactly the expected full name and email address.
        self.assertTrue(User.objects.filter(email=email).exists()) # Account existence: Verifies that an account exists with the submitted email address.
        self.assertEqual(User.objects.filter(email=email).count(), 1) #Account count: Verifies that exactly one account exists with the submitted email address.
    
    def test_privacy_policy_isFalse(self):
        ''' Verifies that sign-up is rejected when the privacy policy is not accepted. '''
        url = reverse('sign-up')
        data = {
            "full_name": "Lisa Meier",
            "email": "lisa.meier@example.de",
            "password": "JoinTest2026!",
            "confirm_password": "JoinTest2026!",
            "privacy_policy": False
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("privacy_policy", response.data) # # Verifies that the response data contains the "privacy_policy" key.
    