## Задание на Python

* Реализовать сервис, который принимает и отвечает на HTTP запросы.

## Описание
* **GET /city/** — получение всех городов из базы
* **POST /city/** — создание города
* **GET /city/city_id/street/** —  получение всех улиц города; (city_id —
идентификатор города)
*  **POST /city/city_id/street/** —  создание улицы в городе; (city_id —
идентификатор города)
* **POST /shop/** —  создание магазина; Данный метод получает json c
объектом магазина, в ответ возвращает данные созданной записи.
* **GET /shop/?street=&city=&open=0/1** — получение списка магазинов
## Подготовительные действия
* Клонировать проект `git clone https://github.com/hvckxm/mediasoft-httpservice-python.git`
* Установить зависимости `pip3 install -r requirements.txt`
* По пути `mediasoft/settings.py` в DATABASES указать свои данные
## Запуск
* Запуск в режиме отладки осуществляется командой `py manage.py runserver`
