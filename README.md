## API_FINAL_YATUBE

Проект представляет из себя API для социальной сети Yatube.


## Примеры доступных эндпоинтов:

- `pi/v1/token/ `- POST: получение JWT-токена;
- `/api/v1/token/refresh/ `- POST: обновление JWT-токена;
- `/api/v1/jwt/verify/ `- POST: проверка JWT-токена;
- `/api/v1/posts/` - GET: получение всех записей, POST: добавление новой записи;
- `/api/v1/posts/{id}/ `- GET: получение записи, PUT: обновление записи, PATCH: частичное обновление записи, DELETE: удаление записи;
- `/api/v1/follow/ `- GET: получение списка всех своих подписок, POST: создание новой подписки;
- `/api/v1/group/ `- GET: получение списка всех групп, POST: создание новой группы
 и другие ...

## Примеры запросов 

Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

`GET http://127.0.0.1:8000/api/v1/posts/`

Ответ:

```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {}
    ]
}
```

Добавление новой публикации в коллекцию публикаций от авторизованного пользователя 

`POST http://127.0.0.1:8000/api/v1/posts/`

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Ответ:

```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:vvgornostaeva/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
