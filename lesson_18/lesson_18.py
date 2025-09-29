# Тестування REST API, 
# частина 1: Робота з мережею. Бібліотеки `urllib` та `requests`. 
# Запити `get, post, put, delete`
import requests
import urllib.request
from urllib.parse import urlparse, urlunparse
from requests.exceptions import HTTPError, ConnectionError, Timeout
# url = "https://www.example.com"
# response = urllib.request.urlopen(url)
# data = response.read()
# print(data)

# url = "https://www.example.com"
# data = {'key1': 'value1', 'key2': 'value2'}
# # Кодуємо дані для POST-запиту
# data = urllib.parse.urlencode(data).encode('utf-8')
# response = urllib.request.urlopen(url, data)
# result = response.read()
# print(result)
url = "https://www.example.com/path/to/resource?param1=value1&param2=value2"

parsed_url = urlparse(url)
print("Схема:", parsed_url.scheme)
print("Мережева адреса:", parsed_url.netloc)
print("Шлях:", parsed_url.path)
print("Параметри:", parsed_url.params)
print("Запити:", parsed_url.query)
print("Фрагмент:", parsed_url.fragment)

scheme = "https"
netloc = "www.example.com"
path = "/path/to/resource"
params = "param1=value1"
query = "param2=value2"
fragment = "section"

composed_url = urlunparse((scheme, netloc, path, params, query, fragment))

print("Складений URL:", composed_url)

url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
response = requests.get(url)
print("Текст", response.text,
      "ск", response.status_code,
      "запиту тіло", response.request.body,
      "урла", response.url,
      "заголовки", response.headers,
      "кукі", response.cookies)
print(response.json())

params = {'postId': 1, 'email': 'Nikita@garfield.biz'}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(response.url)
else:
    print('Помилка запиту:', response.status_code)

data_to_send = {'userId': 10, 'id': 101, 'title': 'Some title'}

response = requests.post(url, data=data_to_send) # data x-form
# response = requests.post(url, json=data_to_send) # json
if response.status_code == 201:
    created_data = response.json()  # отримання даних у форматі JSON
    print('Створено дані:', created_data)
else:
    print('Помилка. Статус-код:', response.status_code)

data_to_put = {'userId': 10, 'id': 101, 'title': 'New title'}
response = requests.put(url, data=data_to_put)
put_data = response.json()  # отримання даних у форматі JSON
print('Пут дані:', put_data)

params = {'userId': 10, 'id': 101, 'title': 'New title'}
response = requests.delete(url, params=params)

# Перевірка статус-коду
if response.status_code == 200:
    print('Дані успішно видалено')
else:
    print('Помилка. Статус-код:', response.status_code)

print(response.headers.get('Content-Type'))
print(response.request.headers)
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0"
headers = {'User-Agent': my_user_agent}
new_response = requests.delete(url, params=params, headers=headers)
print(new_response.request.headers)

try:
    response = requests.get('https://example.com', timeout=5)
    response.raise_for_status()  # Викликає виняток, якщо код не 2xx
except HTTPError as e:
    print('HTTP Помилка:', e)
except ConnectionError as e:
    print('Помилка з\'єднання:', e)
except Timeout as e:
    print('Помилка за часом доступу:', e)

