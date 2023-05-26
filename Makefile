### Defensive settings for make:
#     https://tech.davis-hansson.com/p/make/
SHELL:=bash
.ONESHELL:
.SHELLFLAGS:=-eu -o pipefail -c
.SILENT:
.DELETE_ON_ERROR:
MAKEFLAGS+=--warn-undefined-variables
MAKEFLAGS+=--no-builtin-rules
PS1?=$$


## Top-level targets:

.PHONY: all
### The default target.
all: build

.PHONY: build
### Perform any necessary set-up for local development
build: ./.git/hooks/pre-commit ./var/log/flit-build.log

.PHONY: test
### Test that the package can be installed and run
test: build
	tox run-parallel


## Real Targets:

./var/log/flit-build.log: ./pyproject.toml
	mkdir -pv "$(dir $(@))"
	tox exec -e "build" -- flit build | tee -a "$(@)"

./.git/hooks/pre-commit:
	tox exec -e "build" -- pre-commit install
