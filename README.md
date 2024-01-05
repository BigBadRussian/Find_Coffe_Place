# DEVMAN. Курс Основы Python
## Задание 8. Ищем кофейни
### Описание.
Скрипт показывает на карте 5 ближайших кофеен, зарегистрированных в используемом файле данных "coffee.json"
### Установка и запуск
1. Python3 дожен быть установлен.
2. Скачайте файлы репозитория:  
script.py - python файл с кодом программы  
coffee.json - файл данных о кофейнях в Москве. Содержит открытые данные о нескольких десятках кафэ (название, координаты и т.д.)  
requirements.txt - файл содержит список необходимых к установке библиотек python.  
3. Установите необходимые библиотеки:
```bash
python3 -m venv env 
```
```bash
source env/bin/activate
```
```bash
python3 install -r requirements.txt
```
4. Создайте файл ".env". Это текстовый файл для хранения вашего токена от API Яндекс - геокодер:
```bash
TOKEN=ваш_токен_api-yandex
```
[Получить токен.](https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fdeveloper.tech.yandex.ru%2F&origin=apikeys)  
5. Запустите script.py:
```bash
python3 script.py
```
В вашем интерфейсе появится запрос программы "Где вы находитесь?".
Введите слово, обозначающее географическую точку в Москве, 
например "метро ВДНХ" и нажмите "Enter". 
После чего скрипт отсортирует список кофеен по расстоянию до указанной 
точки (метро ВДНХ) и создаст список из 5 ближайших кофеен, 
нанесет метки кофеен на карту и в вашем интерфейсе появится
ссылка на карту с метками кофеен. Перейдите по ссылке и увидите карту.


Где вы находитесь? 
метро ВДНХ
 * Serving Flask app 'script'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.168.146:5000
Press CTRL+C to quit
192.168.168.146 - - [05/Jan/2024 14:54:08] "GET / HTTP/1.1" 200 -

![](https://github.com/BigBadRussian/Find_Coffe_Place/blob/master/VDNH_coffees_example.png)