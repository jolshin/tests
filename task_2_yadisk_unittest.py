#Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
#Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
#Пример положительных тестов:
#
#Код ответа соответствует 200.
#Результат создания папки - папка появилась в списке файлов.

import requests
from datetime import datetime, date, time
import unittest

class YaDiskExucutor:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        #Method returns headers
        return {
            'Content-Type' : 'application/json',
            'Authorization' : f'OAuth {self.token}'
        }

    def maker(self, path):
        #Method makes folder on yadisk
        request_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path' : path}

        response = requests.put(request_url, headers=headers, params=params)
        
        #below code for debug purposes
        #print(response.json())
        #if response.status_code == 201:
        #   print(f'Папка {path} создана')

        return(response.status_code)

class TestDisCode(unittest.TestCase):
    #Method tests 201 response code - put in correct token
    def test_positive(self):
        token = 'correct_token'
        cur_time = datetime.now().strftime("%H-%M-%S")
        path=f'Netologia_tasks_{cur_time}'

        folder_ops = YaDiskExucutor(token)
        expected = 201
        res = folder_ops.maker(path)
        self.assertEqual(res, expected)
    
    #Method tests 401 response code - put in incorrect token or leave 'bad_token'
    def test_auth_failure(self):
        token = 'bad_token'
        cur_time = datetime.now().strftime("%H-%M-%S")
        path=f'Netologia_tasks_{cur_time}'

        folder_ops = YaDiskExucutor(token)
        
        expected = 401
        res = folder_ops.maker(path)
        self.assertEqual(res, expected)

    #Method tests failure with expect failure decorator - put in incorrect token or leave 'bad_token'
    @unittest.expectedFailure
    def test_failed(self):
        token = 'bad_token'
        cur_time = datetime.now().strftime("%H-%M-%S")
        path=f'Netologia_tasks_{cur_time}'

        folder_ops = YaDiskExucutor(token)
        
        expected = 200
        res = folder_ops.maker(path)
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
    
    #token = 'correct_token'
    #path=f'Netologia_tasks_{datetime.now().strftime("%H-%M-%S")}'

    #folder_ops = YaDiskExucutor(token)
    #folder_ops.maker(path)