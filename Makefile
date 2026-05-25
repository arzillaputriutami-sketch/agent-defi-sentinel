PYTHON ?= python3

.PHONY: test smoke demo markdown

test:
	$(PYTHON) -m pytest -q

smoke:
	$(PYTHON) backend/swarm.py | $(PYTHON) -m json.tool >/dev/null
	$(PYTHON) cli.py --scenario "oracle feed divergence" | $(PYTHON) -m json.tool >/dev/null

demo:
	$(PYTHON) cli.py --all

markdown:
	$(PYTHON) cli.py --scenario "stablecoin depeg pressure" --format markdown
