.PHONY: all gs docker docker-run help

all: help

gs:
	rm -f autograder.zip
	cd source; zip -r ../autograder.zip *

docker: gs
	docker build -t gs_test -f docker/Dockerfile .

docker-run: docker
	cp solution/calculator.c .
	python3 docker/run_docker.py calculator.c
	cat results/results.json | python3 -m json.tool

help:
	@echo "make [all]   -- show this help menu"
	@echo
	@echo "make gs         -- creates autograder.zip for gradescope"
	@echo "make docker     -- builds a gradescope compatible docker image"
	@echo "make docker-run -- runs the docker image to test it"
	@echo
	