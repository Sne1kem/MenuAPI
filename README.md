# MenuAPI
Как запустить проект:
1. Для запуска нужно создать файл .env в корне проекта со следующий содержимым:
   1.1 DB_HOST=localhost
       DB_PORT=5432
       DB_NAME=db
       DB_USER=postgres
       DB_PASS=Pa$$w0rd
2. Выполнить миграции через alembic revision --autogenerate -m 'init' после чего выполнить alembic upgrade head
3. Далее зайти в папку src и выполнить uvicorn main:app --reload
4. Готово, проект запущен
