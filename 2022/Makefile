PYTHON = venv/bin/python3
PYTHON_DIRS = aoc tests


.PHONY: build-deps-amzn
build-deps-amzn:
	sudo yum -y install python-virtualenv

venv:
	virtualenv venv/ --python=python3.7
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -e .

clean:
	rm -fr venv aoc.egg-info

.PHONY: static
static: flake8 pylint mypy

.PHONY: flake8
flake8: venv
	$(PYTHON) -m flake8 --config .flake8 *.py aoc/*.py

.PHONY: mypy
mypy: venv
	$(PYTHON) -m mypy *.py aoc/*.py

.PHONY: pylint
pylint: venv
	$(PYTHON) -m pylint --rcfile .pylintrc *.py aoc/*.py

.PHONY: reformat
reformat: venv
	$(PYTHON) -m isort --atomic $(PYTHON_DIRS)
	$(PYTHON) -m yapf --parallel --recursive --in-place $(PYTHON_DIRS)
	#$(PYTHON) -m black $(PYTHON_DIRS)

.PHONY: tests
tests: venv
	$(PYTHON) -m pytest -s --tb=short tests

