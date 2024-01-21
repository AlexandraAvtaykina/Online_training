Проект Online_training 

Проект онлайн-обучения, разработанный с использованием фреймворка Django.
Технологии:

    python = "^3.10"
    django = "4.2"
    psycopg2-binary = "^2.9.9"
    pillow = "^10.1.0"
    ipython = "^8.18.1"
    djangorestframework = "^3.14.0"
    djangorestframework-simplejwt = "^5.3.1"
    coverage = "^7.3.3"
    drf-yasg = "^1.21.7"
    stripe = "^7.10.0"
    celery = "^5.3.6"
    redis = "^5.0.1"
    django-celery-beat = "^2.5.0"
    docker = "^7.0.0"
    python-dotenv = "^1.0.0"

Запуск проекта

    Склонируйте этот репозиторий к себе

    В проекте используется Poetry, при развертывании локально, он подтянет зависимости автоматически 

    В файле .env.sample заполните необходимые переменные окружения

    Примените миграции:
        python3 manage.py migrate

    Запустите сервер:
        python3 manage.py runserver

    Запустите Celery для обработки отложенных задач:
        celery -A config worker --pool=solo -l INFO
        celery -A config beat -l info -S django

Запуск проекта с помощью Docker:

Для запуска проекта через Docker необходимо:

    Выполнить команды:

    docker-compose build - сборка образа
    docker-compose up - запуск контейнера

Если БД не создана, то необходимо будет ее создать, но перед этим убедиться, что у вас запущен контейнер.

    Команда для создания БД: docker-compose exec db psql -U postgres
