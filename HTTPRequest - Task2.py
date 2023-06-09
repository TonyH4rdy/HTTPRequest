from pprint import pprint
import requests

class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": True }
        response = requests.get(upload_url, headers=headers, params=params)

        return response.json()
    # Функция , загружающая файл на Яндекс-диск :
    def upload(self, file_path: str):
        data_link = self._get_upload_link(disk_file_path=file_path)

        url = data_link.get("href")

        response = requests.put(url, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл успешно загружен")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'My_file_homework.txt'
    token = "..."
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
