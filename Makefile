.PHONY: clean install run all

clean:
	@echo "Delete byte files"
	find . -type f -name '*.pyc' -delete

install:
	@echo "Install dependencies"
	pipenv install

flask:
	@echo "Run flask api"
	env PYTHONPATH=$(PWD) pipenv run python ./slashcommands/flask/api.py

celery:
	@echo "Run celery worker"
	env PYTHONPATH=$(PWD) pipenv run celery -A slashcommands.celery worker --loglevel=debug

all: clean install run
