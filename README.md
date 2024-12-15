## Описание

Этот проект представляет собой веб-приложение, разработанное с использованием Django и Django REST Framework. Он включает в себя модели для управления контактами, сетями и продуктами, а также предоставляет API для взаимодействия с этими моделями.

## Установка

## Предварительные требования

- Python 3.12 или выше
- PostgreSQL 
- Poetry для управления зависимостями

## Клонирование репозитория

```
git clone https://github.com/yufilchakov/certification
cd certification
```

## Установка зависимостей
Убедитесь, что у вас установлен Poetry. Затем выполните:
```
poetry install
```

## Настройка базы данных
Создайте базу данных в PostgreSQL.
Настройте параметры подключения в файле config/settings.py.

## Миграции
Примените миграции для создания необходимых таблиц в базе данных:
```
python manage.py migrate
```
## Запуск сервера
Запустите сервер разработки:
```
python manage.py runserver
```
Теперь вы можете получить доступ к приложению по адресу http://127.0.0.1:8000/.

## API

### Эндпоинты

#### Контакты

GET /api/contacts/ - Получить список контактов

POST /api/contacts/ - Создать новый контакт

GET /api/contacts/{id}/ - Получить контакт по ID

PUT /api/contacts/{id}/ - Обновить контакт по ID

DELETE /api/contacts/{id}/ - Удалить контакт по ID

#### Сети

GET /api/network/ - Получить список сетей

POST /api/network/ - Создать новую сеть

GET /api/network/{id}/ - Получить сеть по ID

PUT /api/network/{id}/ - Обновить сеть по ID

DELETE /api/network/{id}/ - Удалить сеть по ID

#### Продукты

GET /api/products/ - Получить список продуктов

POST /api/products/ - Создать новый продукт

GET /api/products/{id}/ - Получить продукт по ID

PUT /api/products/{id}/ - Обновить продукт по ID

DELETE /api/products/{id}/ - Удалить продукт по ID