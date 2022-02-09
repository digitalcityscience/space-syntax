TAG=ghcr.io/digitalcityscience/space-syntax

help:
	@echo "for now, you are on your own"

init:
	python3 -m venv --prompt space-syntax .venv
	source .venv/bin/activate 

install:
	pip install -r requirements-dev.txt

install-mac:
	brew install gdal proj geos --force
	install

test: test/*.py
	python -m pytest -ra

docker:
	docker build --network=host -t ${TAG}:latest .

rebuild-docker:
	docker build --network=host -t ${TAG}:latest .

run:
	python -m main

run-docker: 
	docker run --rm -v "${PWD}"/workdir:/home/app/downloads ${TAG}

debug-docker:
	docker run --network=host --rm -v "${PWD}"/workdir:/home/app/downloads -it --entrypoint /bin/bash  ${TAG}

clean:
	rm -rf downloads/

