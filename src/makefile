.PHONY: clean

NAME 	   	:= Logica Difusa
VERSION		:= 2.0
DEVELOPERS	:= Ariel Plasencia
COPYRIGHT  	:= Copyright © 2022: $(DEVELOPERS)

main: ## Compiling the project :)
	@echo "Compiling the project :)"

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

install: ## Install the project dependencies
	pip install math
	pip install numpy

clean: ## Remove temporary files
	rm -rf fuzzy/__pycache__
	rm -rf utils/__pycache__

run: ## Run the project
	python main.py

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'