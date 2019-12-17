from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group

class GroupTests(APITestCase):
    def test_create_group(self):
        """
        Ensure we can create a new group object.
        """
        url = reverse('group-list')
        data = {'name': 'test_one'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(Group.objects.get().name, 'test_one')