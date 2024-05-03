import unittest
import json
from app import app

class TestKeyValueAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_key_value(self):
        # Отправляем POST запрос для создания объекта
        response = self.app.post('/keyvalue', json={'key': 'test_key', 'value': 'test_value'})
        data = json.loads(response.data.decode('utf-8'))
        # Проверяем код ответа и ожидаемый результат
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Key test_key set to value test_value')

    def test_read_key_value(self):
        # Отправляем GET запрос для чтения объекта
        response = self.app.get('/keyvalue/test_key')
        data = json.loads(response.data.decode('utf-8'))
        # Проверяем код ответа и ожидаемый результат
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'key': 'test_key', 'value': 'test_value'})

    def test_update_key_value(self):
        # Отправляем PUT запрос для обновления значения объекта
        response = self.app.put('/keyvalue', json={'key': 'test_key', 'value': 'updated_value'})
        data = json.loads(response.data.decode('utf-8'))
        # Проверяем код ответа и ожидаемый результат
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Key test_key set to value updated_value')

if __name__ == '__main__':
    unittest.main()
