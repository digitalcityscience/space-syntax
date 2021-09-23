help:
	@echo "for now, you are on your own"

init:
	python3 -m venv --prompt space-syntax .venv
	source .venv/bin/activate 

build:
	pip install -r requirements.txt

run:
	python -m download

