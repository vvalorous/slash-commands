.PHONY: clean install run all

clean:
	find . -type f -name '*.pyc' -delete

install:
	pipenv install

run:
	env PYTHONPATH=$(PWD) pipenv run python ./slashcommands/flask/api.py

all: clean install run
