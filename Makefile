# Define variables
PYTHON := python3
SCRIPT := sudoku.py

# Set the default goal to 'run'
.DEFAULT_GOAL := run

# Default target
.PHONY: run
run:
	@$(PYTHON) $(SCRIPT)

# Usage instructions
.PHONY: help
help:
	@echo "help"
