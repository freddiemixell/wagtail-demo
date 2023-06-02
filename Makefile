dev:
	python manage.py runserver 0:8000

migrations:
	python manage.py makemigrations && python manage.py migrate

migrate:
	python manage.py migrate