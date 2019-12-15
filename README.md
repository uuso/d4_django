# d4_django
Some practice with django framework

Created a few models, simple views and a pair of templates.

Для локального использования потребуется внутри виртуального окружения определить переменные окружения SECRET_KEY и LOCAL_DB и дать им непустые значения.

Согласно заданию, приложение умеет:
1. создавать издательства, авторов и книги
2. регистрировать личность для сдачи книги на время

### Usage:
```
export SECRET_KEY="qwe"
export LOCAL_DB="qwe"
python ./manage.py migrate
python ./manage.py loaddata data_d5.xml
python ./manage.py runserver
```
### URLs:

http://127.0.0.1:8000/index - default tableview

http://127.0.0.1:8000/admin:
one:one
