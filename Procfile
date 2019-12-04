release: python manage.py migrate
release: echo "MIGRATED!\n"
release: python manage.py loaddata data1.xml
web: python manage.py runserver 0.0.0.0:$PORT
