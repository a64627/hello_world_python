install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
test:
	python -m pytest -vv --cov=hello_world hello_world_test.py

lint:
	pylint --disable=R,C hello_world.py
	
all: install lint test