.DEFAULT_GOAL := help

PORT ?= 8000
HOST ?= 127.0.0.1

.PHONY: dev test lint typecheck help start stop status restart

dev:       ## Sync the environment (project + dev group, from the lock)
	uv sync

test:      ## Run the test suite
	uv run pytest

lint:      ## Ruff over src/ and tests/
	uv run ruff check src/ tests/

typecheck: ## Pyright over the tree's [tool.pyright] include set
	uv run pyright

start:     ## Start the server in the background (run from the repo root; pid -> .prioritree/server.pid; override: make start PORT=8100)
	@if [ -f .prioritree/server.pid ] && kill -0 $$(cat .prioritree/server.pid) 2>/dev/null; then \
		echo "start refused: expected no live pid, found pid $$(cat .prioritree/server.pid) live (the server is running); next-action: make status, or make stop"; \
		exit 1; \
	fi
	@if [ ! -x .venv/bin/uvicorn ]; then \
		echo "start refused: expected .venv/bin/uvicorn, found it absent (no venv yet); next-action: make dev (uv sync) first"; \
		exit 1; \
	fi
	@mkdir -p .prioritree
	@nohup env -u WEB_CONCURRENCY .venv/bin/uvicorn prioritree.service:app --host $(HOST) --port $(PORT) > .prioritree/server.log 2>&1 & echo $$! > .prioritree/server.pid
	@sleep 1; curl -s -o /dev/null -w 'read-back: HTTP %{http_code} on http://127.0.0.1:$(PORT)/ (404 = answering; 000 = still booting: make status)\n' http://127.0.0.1:$(PORT)/runs/RUN-0001/next || true

stop:      ## Stop the server: SIGTERM + the bounded drain (pid read from .prioritree/server.pid; run from the repo root)
	@if [ ! -f .prioritree/server.pid ]; then echo "stop: no pidfile; nothing managed (already down)"; exit 0; fi
	@pid=$$(cat .prioritree/server.pid); \
	if ! kill -0 $$pid 2>/dev/null; then \
		echo "stop refused: expected a live pid, found pid $$pid dead (stale pidfile); next-action: the stale pidfile is removed; make start launches fresh"; \
		rm -f .prioritree/server.pid; \
		exit 1; \
	fi; \
	echo "SIGTERM -> pid $$pid (the graceful drain)"; \
	kill $$pid; \
	i=0; \
	while kill -0 $$pid 2>/dev/null && [ $$i -lt 5 ]; do sleep 1; i=$$((i + 1)); done; \
	rm -f .prioritree/server.pid; \
	if kill -0 $$pid 2>/dev/null; then \
		echo "stop incomplete: expected the pid gone by the 5s bound, found pid $$pid still live; next-action: make status, or kill -9 $$pid"; \
		exit 1; \
	else \
		echo "stopped: pid $$pid gone (the pidfile is removed)"; \
	fi
	@curl -s -o /dev/null http://127.0.0.1:$(PORT)/runs/RUN-0001/next && echo "read-back: STILL ANSWERING on $(PORT); another (unmanaged) server holds the port" || echo "read-back: refused on $(PORT) - the port is down"

status:    ## Report the pid and the port, both labeled, read-only (run from the repo root)
	@if [ -f .prioritree/server.pid ]; then \
		pid=$$(cat .prioritree/server.pid); \
		if kill -0 $$pid 2>/dev/null; then echo "pid: $$pid (live)"; else echo "pid: $$pid (dead; stale pidfile; next-action: make stop cures it)"; fi; \
	else \
		echo "pid: none (no pidfile; not managed)"; \
	fi
	@code=$$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:$(PORT)/runs/RUN-0001/next); \
	if [ "$$code" = "404" ]; then echo "port: $(PORT) answering (HTTP 404 on /runs/RUN-0001/next; the ready form)"; \
	elif [ "$$code" = "000" ]; then echo "port: $(PORT) refused (down)"; \
	else echo "port: $(PORT) answered HTTP $$code (unexpected; not the ready form)"; \
	fi

restart: stop start ## Stop then start: the operator's rebind (run from the repo root; the read-backs ride both prerequisites)

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
