import unittest

import requests

from my_token import token_ya


class TestCreateYaFolder(unittest.TestCase):
    def test_create_folder(self):
        folder_name = 'test_folder'
        url_const = 'https://cloud-api.yandex.net/v1/disk/resources?path='
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token_ya}'}
        url_folder = url_const + folder_name
        response_put = requests.put(url_folder, headers=headers)
        self.assertEqual(response_put.status_code, 201)

        url_root = url_const + '/'
        response_root = requests.get(url_root, headers=headers).json()
        files_list = [item['name'] for item in response_root["_embedded"]['items']]
        self.assertIn(folder_name, files_list)

        response_get = requests.get(url_folder, headers=headers)
        self.assertEqual(response_get.status_code, 200)

        requests.delete(url_folder, headers=headers)

    def test_not_authorized(self):
        folder_name = 'test_folder'
        non_valid_token = 'non_valid_token'
        url_const = 'https://cloud-api.yandex.net/v1/disk/resources?path='
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {non_valid_token}'}
        url_folder = url_const + folder_name
        response_put = requests.put(url_folder, headers=headers)
        self.assertEqual(response_put.status_code, 401)

    def test_path_exist(self):
        folder_name = 'test_folder'
        url_const = 'https://cloud-api.yandex.net/v1/disk/resources?path='
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token_ya}'}
        url_folder = url_const + folder_name
        requests.put(url_folder, headers=headers)
        response_put = requests.put(url_folder, headers=headers)
        self.assertEqual(response_put.status_code, 409)
        requests.delete(url_folder, headers=headers)