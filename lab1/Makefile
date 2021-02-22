.PHONY: build start stop purge

APP_NAME := country-info
SHELL := /bin/bash
SOURCES := $(shell find . -name '*.py' -not -path '*./.venv/*' -not -path '*./.git/*' -print)

all: lint

venv: .venv/bin/activate

.venv/bin/activate: requirements.txt
	@python3 -m venv ./.venv
	@.venv/bin/python -m pip install -r requirements.txt
	@touch .venv/bin/activate

black: venv
	@.venv/bin/black --target-version=py38 --line-length=100 -- $(SOURCES)

lint: venv
	-.venv/bin/pylint -- $(SOURCES)
	-.venv/bin/flake8 -- $(SOURCES)


#DOCKER
docker-build:
	@docker build --tag $(APP_NAME) $(PWD)

docker-start:
	@docker run --it --name=$(APP_NAME) $(APP_NAME)

docker-stop:
	@docker stop $(APP_NAME) && docker rm $(APP_NAME)

docker-purge:
	-docker rm --force $(shell docker ps --all --quiet) > /dev/null 2>&1
	-docker rmi --force $(shell docker images --all --quiet) > /dev/null 2>&1
