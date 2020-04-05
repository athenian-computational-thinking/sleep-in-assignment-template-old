default: run

run:
	python3 my_code.py

test:
	pytest

tests: test

clean:
	rm *.pyc