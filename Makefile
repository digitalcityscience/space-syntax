TAG=ghcr.io/digitalcityscience/space-syntax
FAASD_TAG=${TAG}-faasd

help:
	@echo "for now, you are on your own"

init:
	python3 -m venv --prompt space-syntax .venv
	source .venv/bin/activate 

build:
	pip install -r requirements.txt

docker:
	docker build . --network=host --tag ${TAG}:latest

docker-faasd:
	docker build . --tag ${FAASD_TAG} --file Dockerfile-faasd

rebuild-docker:
	docker build --network=host -t ${TAG}:latest .

run:
	python -m main

run-docker: 
	docker run --rm -v "${PWD}"/workdir:/home/app/downloads ${TAG}

run-faasd-docker:
	docker run --rm -p 8080:8080 ${FAASD_TAG}
clean:
	rm -rf downloads/


