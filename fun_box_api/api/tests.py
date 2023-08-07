from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory


class PostTest(APITestCase):
    def test_append_sites(self):
        url = ('/api/append')
        data = {
            "links": [
                "https://ya.ru",
                "https://ya.ru?q=123",
                "fuuuuuuunbox.ru",
                "funbox.ru",
                "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_sites(self):
        url = ('/api/get_sites')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
