help:
	@echo "for now, you are on your own"

init:
	python3 -m venv --prompt space-syntax .venv
	source .venv/bin/activate 

build:
	pip install -r requirements.txt

build-docker:
	docker build -t dcs/space-syntax .

run:
	python -m main

run-docker: 
	docker run -v "${PWD}"/workdir:/home/app/downloads -it dcs/space-syntax

clean:
	rm -rf downloads/

