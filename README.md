Запуск проекта

    docker-compose up web

Запуск тестов

    docker-compose up test

Заполнить базу

    docker-compose up filldb

В результате будут применены миграции, база 
будет заполнена тестовыми значениями и будет 
создан суперпользователь
логин: admin
пароль: 1qaz2wsx3edc

Запустить линтер

    docker-compose up lint