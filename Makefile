.PHONY: help requirements test_requirements test

test: test.sandbox test.tools

test.%:
	python deploy_pipelines.py $* -f config.yml --dry-run

requirements:
	pip install -r requirements.txt

test_requirements: requirements
	pip install -r requirements/test_requirements.txt
