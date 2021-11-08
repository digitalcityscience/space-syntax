help:
	@echo "for now, you are on your own"

init:
	python3 -m venv --prompt space-syntax .venv
	source .venv/bin/activate 

build:
	pip install -r requirements.txt

build-docker:
	docker build --no-cache --network=host -t dcs/space-syntax:latest .

build-docker-faasd:
	docker build  --no-cache --network=host -t digitalcityscience/space-syntax -f faasd/Dockerfile .

rebuild-docker:
	docker build --network=host -t dcs/space-syntax:latest .

run:
	python -m main

run-docker: 
	docker run -v "${PWD}"/workdir:/home/app/downloads -it dcs/space-syntax

clean:
	rm -rf downloads/

