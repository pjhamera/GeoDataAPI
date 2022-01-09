from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.test import APIClient
from .models import GeoData

class GeoDataListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_example515', password='TestPassword123')
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')

    def test_geodata_list(self):
        response = self.client.get(reverse('geodata-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_geodata_add(self):
        data = {
                    "ip": "104.26.7.173",
                    "url": "https://gazetakrakowska.pl",
                    "continent_code": "NA",
                    "country_name": "VA",
                    "region_name": "Virginia",
                    "city": "Ashburn",
                    "zip": "20147",
                    "latitude": 39.043701171875,
                    "longitude": -77.47419738769531,
                    "is_eu": "false"
                }
        response = self.client.post(reverse('geodata-add'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_geodata_delete(self):
        self.geodata = GeoData.objects.create(
            ip = "104.26.7.173", 
            url = "https://gazetakrakowska.pl",
            continent_code = "NA",
            country_name = "VA",
            region_name = "Virginia",
            city = "Ashburn",
            zip = "20147",
            latitude = 39.043701171875,
            longitude = -77.47419738769531,
            is_eu = False
            )
        response = self.client.delete(reverse('geodata-ip', args=(self.geodata.ip,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_geodata_get_url(self):
        self.geodata = GeoData.objects.create(
            ip = "104.26.7.173", 
            url = "https://gazetakrakowska.pl",
            continent_code = "NA",
            country_name = "VA",
            region_name = "Virginia",
            city = "Ashburn",
            zip = "20147",
            latitude = 39.043701171875,
            longitude = -77.47419738769531,
            is_eu = False
            )
        response = self.client.get(reverse('geodata-url', args=(self.geodata.url,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
