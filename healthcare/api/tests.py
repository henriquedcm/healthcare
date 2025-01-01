from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from healthcare.api.models import Patient


class PatientTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username="admin", password="test")
        self.client.force_login(user)

    def test_create_patient(self):
        url = reverse("patient-list")
        payload = {
            "name": [{"use": "usual", "family": "Surname", "given": ["First Name"]}],
            "gender": "male",
            "birth_date": "2000-01-01",
            "address": [
                {
                    "city": "My City",
                    "state": "My State",
                    "postalCode": "1234-000",
                    "use": "home",
                    "type": "physical",
                }
            ],
            # "resourceType": "Patient",
            "telecom": [
                {"system": "email", "value": "patient@mail.com", "use": "home"}
            ],
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
