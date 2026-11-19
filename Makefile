.DEFAULT_GOAL := help

.PHONY: dev test lint typecheck help

dev:       ## Sync the environment (project + dev group, from the lock)
	uv sync

test:      ## Run the test suite
	uv run pytest

lint:      ## Ruff over src/ and tests/
	uv run ruff check src/ tests/

typecheck: ## Pyright over the tree's [tool.pyright] include set
	uv run pyright

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
