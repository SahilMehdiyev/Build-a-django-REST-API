run_server:
	poetry run python manage.py runserver
run_algolia:
	poetry run python manage.py algolia_reindex

shell:
	poetry run python manage.py shell
create_superuser:
	poetry run python manage.py createsuperuser

run_detail:
	poetry run python py_client/detail.py

run_test:
	poetry run python manage.py test

run_basic:
	poetry run python py_client/basic.py	

run_list:
	poetry run python py_client/list.py

run_update:
	poetry run python py_client/update.py

run_create:
	poetry run python py_client/create.py

run_not_found:
	poetry run python py_client/not_found.py

run_migrate:
	poetry run python manage.py migrate
run_makemigrations:
	poetry run python manage.py makemigrations

pre_commit_run:
	pre-commit run --files

install:
	poetry install

.PHONY: run_server,create_superuser
.PHONY: run_migrate,run_makemigrations
.PHONY: install
.PHONY: pre_commit_run
.PHONY: shell