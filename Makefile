
make_venv:
	if [ ! -d .venv ]; then virtualenv -p `which python3` .venv; fi; \
	. .venv/bin/activate; \
	which python; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	deactivate

make_migr:
	. .venv/bin/activate; \
	python manage.py makemigrations; \
	deactivate

migr:
	. .venv/bin/activate; \
	python manage.py migrate; \
	deactivate

test:
	. .venv/bin/activate; \
	python manage.py test; \
	deactivate

super:
	. .venv/bin/activate; \
	python manage.py createsuperuser; \
	deactivate

shell:
	. .venv/bin/activate; \
	python manage.py shell; \
	deactivate

run:
	. .venv/bin/activate; \
	# python manage.py collectstatic; \
	python manage.py runserver 0.0.0.0:18000; \
	deactivate
