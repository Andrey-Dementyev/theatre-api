from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "testpass123",
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_create_user_success(self):
        url = reverse("user:create")
        data = {"email": "newuser@example.com", "password": "newpassword123"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("email", response.data)
        self.assertNotIn("password", response.data)

    def test_create_user_invalid_data(self):
        url = reverse("user:create")
        data = {"email": "", "password": ""}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_obtain_pair(self):
        url = reverse("user:token_obtain_pair")
        response = self.client.post(url, self.user_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_token_refresh(self):
        url = reverse("user:token_obtain_pair")
        response = self.client.post(url, self.user_data)
        refresh_token = response.data["refresh"]

        url = reverse("user:token_refresh")
        response = self.client.post(url, {"refresh": refresh_token})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_manage_user_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("user:manage")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_manage_user_unauthenticated(self):
        url = reverse("user:manage")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
