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
build: ./.git/hooks/pre-commit ./var/log/poetry-install.log


## Real Targets:

./var/log/poetry-install.log: ./pyproject.toml
	mkdir -pv "$(dir $(@))"
	tox exec -e "build" -- poetry install | tee -a "$(@)"

./.git/hooks/pre-commit:
	tox exec -e "build" -- pre-commit install
