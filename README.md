# MenuAPI
Как запустить проект:
СПЕРВА НУЖНО СОЗДАТЬ БАЗУ ДАННЫЙ В POSTGRESQL
1. psql -U (имя пользователя)
2. Укажите пароль для входа
3. CREATE DATABASE 'Имя создаваемой базы'; - не забудьте точку с запятой

Активация окружения и загрузка зависимостей:
1. python -m venv venv в корне проекта
2. source venv/Scripts/Activate - для активации окружения
3. pip install -r requirements.txt - для загрузки всех необходимых пакетов

1. Для запуска нужно создать файл .env в корне проекта со следующий содержимым:
   1.1 DB_HOST=localhost
       DB_PORT=5432
       DB_NAME=ИМЯ БАЗЫ
       DB_USER=ИМЯ ПОЛЬЗОВАТЕЛЯ БАЗЫ
       DB_PASS=ПАРОЛЬ ПОЛЬЗОВАТЕЛЯ БАЗЫ
3. Выполнить миграции через alembic revision --autogenerate -m 'init' после чего выполнить alembic upgrade head
4. Далее зайти в папку src и выполнить uvicorn main:app --reload
5. Готово, проект запущен
