.PHONY: clean install run all

clean:
	find . -type f -name '*.pyc' -delete

install:
	pipenv install

run:
	env PYTHONPATH=$(PWD) pipenv run python ./slashcommands/api/api.py

all: clean install run
