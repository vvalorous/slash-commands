flask:
	pipenv run flask run

celery:
	pipenv run celery -A slash_commands.celery worker --loglevel=debug
