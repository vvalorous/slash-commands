.phony: clean install flask celery

clean:
	@echo 'Removing byte files...'
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type f -name '*.log*' -delete

install:
	@echo 'Installing dependencies...'
	pipenv install

flask:
	@echo 'Running flask api...'
	pipenv run flask run

celery:
	@echo 'Running celery worker...'
	pipenv run celery -A slash_commands.celery worker --loglevel=debug

all: clean install
