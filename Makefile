PWD := $(or $(PWD), `pwd`)
#Example for Windows: make touch-pristine-project PWD=%cd%

.DEFAULT:
	echo Uh oh! The target does not exist.

.SILENT:

.PHONE: django-admin da
django-admin da:
	docker-compose exec api bash -c "python manage.py $(or $(COMMAND), $(CMD))"

.PHONY: django-app dapp
django-app dapp:
	docker-compose exec api bash -c "mkdir -p apps/$(or $(NAME), $(APP)) && python manage.py startapp $$NAME ./apps/$(or $(NAME), $(APP))"

.PHONY: django-migrate migrate dm
django-migrate migrate dm:
	docker-compose exec -T api bash -c "python manage.py migrate"

.PHONY: django-make-migrations
django-make-migrations:
	docker-compose exec -T api bash -c "python manage.py makemigrations"

.PHONY: django-shell ds
django-shell ds:
	docker-compose exec -T api bash -c "python manage.py shell_plus"

.PHONY: django-superuser superuser su
django-superuser superuser su:
	docker-compose exec api bash -c "python manage.py createsuperuser"

.PHONY: lint-check lint lc
lint-check lint lc:
	docker-compose exec -T api bash -c "pylint --rcfile=/var/config/pylintrc ./apps ./backend"

.PHONY: security-check security sc
security-check security sc:
	docker-compose exec -T api bash -c "bandit -c /var/config/bandit.conf -r ."

.PHONY: test t
test t:
	docker-compose exec -T api bash -c "pytest -c /var/config/pytest.ini --disable-warnings"

.PHONY: test-with-coverage test-coverage tc
test-with-coverage test-coverage tc:
	docker-compose exec api bash -c "coverage run --rcfile=/project-config/.coveragerc && cd /project-generated/coverage && coverage html"













##################### ^^^^^^^ TESTED ^^^^^^^^^^ #######################







.PHONY: django-database-seed
django-database-seed:
	echo "\033[31mThis is a destructive command. It will drop your current database and rebuild it with seeded data."
	echo "\033[31mIf this is not what you want, you have 10 seconds to kill this command with control + c"
	sleep 10
	echo "\033[31mTimes up!"
	$(MAKE) docker-down
	$(MAKE) docker-remove-volumes
	$(MAKE) docker-upd
	(python3 scripts/wait_for_web_container.py && $(MAKE) django-admin COMMAND="seed_db --multiplier $$MULTIPLIER" && $(MAKE) docker-up) || $(MAKE) docker-down;



.PHONY: docker-down
docker-down:
	docker-compose down --remove-orphans

.PHONY: docker-remove-volumes
docker-remove-volumes:
	docker-compose down -v

.PHONY: docker-terminal
docker-terminal:
	docker-compose exec $$CONTAINER bash

.PHONY: docker-terminal-API
docker-terminal-API:
	$(MAKE) docker-terminal CONTAINER=API

.PHONY: docker-up
docker-up:
	docker-compose up

.PHONY: docker-upb
docker-upb:
	docker-compose up --build

.PHONY: docker-upd
docker-upd:
	docker-compose up -d

.PHONY: install-dev-package
install-dev-package:
	$(MAKE) docker-down
	docker run -v "$(PWD)"/config:/config --rm -it python:3.8 bash -c "cd /config && pip install pipenv && pipenv install --dev $$PACKAGE"
	$(MAKE) docker-upb

.PHONY: install-prod-package
install-prod-package:
	$(MAKE) docker-down
	docker run -v "$(PWD)"/config:/config --rm -it python:3.8 bash -c "cd /config && pip install pipenv && pipenv install $$PACKAGE"
	$(MAKE) docker-upb

.PHONY: new-project
new-project:
	cd .. && django-admin startproject --template ./ --extension * --name * backend



.PHONY: touch-pristine-project
touch-pristine-project:
	docker run -v "$(PWD)":/backend --rm -it python:3 bash -c "cd /backend && python3 scripts/setup_new_project.py"
