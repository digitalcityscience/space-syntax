TAG=ghcr.io/digitalcityscience/space-syntax

help:
	@echo "for now, you are on your own"

init:
	python3 -m venv --prompt space-syntax .venv
	source .venv/bin/activate 

build:
	pip install -r requirements.txt

build-docker:
	docker build --network=host -t ${TAG}:latest .

rebuild-docker:
	docker build --network=host -t ${TAG}:latest .

run:
	python -m main

run-docker: 
	docker run --rm -v "${PWD}"/workdir:/home/app/downloads ${TAG}

clean:
	rm -rf downloads/

