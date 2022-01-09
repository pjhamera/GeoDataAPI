from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "TestPasssword123",
            "password2": "TestPasssword123"
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)