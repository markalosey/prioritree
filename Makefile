.DEFAULT_GOAL := help

PORT ?= 8000
HOST ?= 127.0.0.1
MCP_PORT ?= 8100
MCP_HOST ?= 127.0.0.1
AUTH ?= on
PRIORITYTREE_WEB_KEY ?=

.PHONY: dev test lint typecheck help start stop status restart mcp-start mcp-stop mcp-status mcp-restart

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
	@nohup env -u WEB_CONCURRENCY AUTH=$(AUTH) PRIORITYTREE_WEB_KEY=$(PRIORITYTREE_WEB_KEY) .venv/bin/uvicorn prioritree.service:app --host $(HOST) --port $(PORT) > .prioritree/server.log 2>&1 & echo $$! > .prioritree/server.pid
	@sleep 1; curl -s -o /dev/null -w 'read-back: HTTP %{http_code} on http://127.0.0.1:$(PORT)/ (404 = answering; 000 = still booting: make status)\n' http://127.0.0.1:$(PORT)/runs/RUN-9999/next || true

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
	@curl -s -o /dev/null http://127.0.0.1:$(PORT)/runs/RUN-9999/next && echo "read-back: STILL ANSWERING on $(PORT); another (unmanaged) server holds the port" || echo "read-back: refused on $(PORT) - the port is down"

status:    ## Report the pid and the port, both labeled, read-only (run from the repo root)
	@if [ -f .prioritree/server.pid ]; then \
		pid=$$(cat .prioritree/server.pid); \
		if kill -0 $$pid 2>/dev/null; then echo "pid: $$pid (live)"; else echo "pid: $$pid (dead; stale pidfile; next-action: make stop cures it)"; fi; \
	else \
		echo "pid: none (no pidfile; not managed)"; \
	fi
	@code=$$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:$(PORT)/runs/RUN-9999/next); \
	if [ "$$code" = "404" ]; then echo "port: $(PORT) answering (HTTP 404 on /runs/RUN-9999/next; the ready form)"; \
	elif [ "$$code" = "000" ]; then echo "port: $(PORT) refused (down)"; \
	else echo "port: $(PORT) answered HTTP $$code (unexpected; not the ready form)"; \
	fi

restart: stop start ## Stop then start: the operator's rebind (run from the repo root; the read-backs ride both prerequisites)

mcp-start: ## Start the MCP server in the background (run from the repo root; pid -> .prioritree/mcp-server.pid; override: make mcp-start MCP_PORT=<other>)
	@if [ -f .prioritree/mcp-server.pid ] && kill -0 $$(cat .prioritree/mcp-server.pid) 2>/dev/null; then \
		echo "mcp-start refused: expected no live pid, found pid $$(cat .prioritree/mcp-server.pid) live (the MCP server is running); next-action: make mcp-status, or make mcp-stop"; \
		exit 1; \
	fi
	@if [ ! -x .venv/bin/python ]; then \
		echo "mcp-start refused: expected .venv/bin/python, found it absent (no venv yet); next-action: make dev (uv sync) first"; \
		exit 1; \
	fi
	@mkdir -p .prioritree
	@nohup env -u WEB_CONCURRENCY AUTH=$(AUTH) .venv/bin/python -m prioritree.mcp_server --serve --host $(MCP_HOST) --port $(MCP_PORT) > .prioritree/mcp-server.log 2>&1 & echo $$! > .prioritree/mcp-server.pid
	@sleep 1; code=$$(curl -s -o /dev/null -w '%{http_code}' -m 2 http://127.0.0.1:$(MCP_PORT)/mcp || true); echo "read-back: HTTP $$code on http://127.0.0.1:$(MCP_PORT)/mcp (400 = answering (the MCP protocol's bare-GET refusal — the server enforcing its protocol); 000 = still booting: make mcp-status)"

mcp-stop:  ## Stop the MCP server: SIGTERM + the bounded drain (pid read from .prioritree/mcp-server.pid; run from the repo root)
	@if [ ! -f .prioritree/mcp-server.pid ]; then echo "mcp-stop: no pidfile; nothing managed (already down)"; exit 0; fi
	@pid=$$(cat .prioritree/mcp-server.pid); \
	if ! kill -0 $$pid 2>/dev/null; then \
		echo "mcp-stop refused: expected a live pid, found pid $$pid dead (stale pidfile); next-action: the stale pidfile is removed; make mcp-start launches fresh"; \
		rm -f .prioritree/mcp-server.pid; \
		exit 1; \
	fi; \
	echo "SIGTERM -> pid $$pid (the graceful drain)"; \
	kill $$pid; \
	i=0; \
	while kill -0 $$pid 2>/dev/null && [ $$i -lt 5 ]; do sleep 1; i=$$((i + 1)); done; \
	rm -f .prioritree/mcp-server.pid; \
	if kill -0 $$pid 2>/dev/null; then \
		echo "mcp-stop incomplete: expected the pid gone by the 5s bound, found pid $$pid still live; next-action: make mcp-status, or kill -9 $$pid"; \
		exit 1; \
	else \
		echo "stopped: pid $$pid gone (the pidfile is removed)"; \
	fi
	@code=$$(curl -s -o /dev/null -w '%{http_code}' -m 2 http://127.0.0.1:$(MCP_PORT)/mcp); \
	if [ "$$code" = "000" ]; then echo "read-back: refused on $(MCP_PORT) - the port is down"; \
	else echo "read-back: STILL ANSWERING on $(MCP_PORT) (HTTP $$code); another (unmanaged) server holds the port"; \
	fi

mcp-status: ## Report the MCP server's pid and port, both labeled, read-only (run from the repo root)
	@if [ -f .prioritree/mcp-server.pid ]; then \
		pid=$$(cat .prioritree/mcp-server.pid); \
		if kill -0 $$pid 2>/dev/null; then echo "pid: $$pid (live)"; else echo "pid: $$pid (dead; stale pidfile; next-action: make mcp-stop cures it)"; fi; \
	else \
		echo "pid: none (no pidfile; not managed)"; \
	fi
	@code=$$(curl -s -o /dev/null -w '%{http_code}' -m 2 http://127.0.0.1:$(MCP_PORT)/mcp); \
	if [ "$$code" = "400" ]; then echo "port: $(MCP_PORT) answering at /mcp (HTTP $$code; the protocol's bare-GET refusal — the ready form)"; \
	elif [ "$$code" = "000" ]; then echo "port: $(MCP_PORT) refused (down)"; \
	else echo "port: $(MCP_PORT) answered HTTP $$code (unexpected; the ready form is 400)"; \
	fi

mcp-restart: mcp-stop mcp-start ## Stop then start: the operator's rebind (run from the repo root; the read-backs ride both prerequisites)

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
