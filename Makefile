# Define variables
PYTHON := python3
SCRIPT := src/sudoku.py

# Set the default goal to 'run'
.DEFAULT_GOAL := run

# Default target
.PHONY: run
run:
	@$(PYTHON) $(SCRIPT) $(ARGS)

# Usage instructions
.PHONY: help
help:
	@echo "help"


ARGS ?= -g 1 17