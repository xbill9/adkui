# Makefile for ADK Comic Pipeline

.PHONY: clean test deploy run

clean:
	@echo "Cleaning up generated images and temporary files..."
	find . -name "*.log" -delete 2>/dev/null || true
	find images -name "*.png" -delete 2>/dev/null || true
	find output/images -name "*.png" -delete 2>/dev/null || true
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".adk" -exec rm -rf {} +
	@echo "Clean completed."

test:
	@echo "Running comic generation validation..."
	python3 fix_comic.py

deploy:
	@echo "Deploying the comic pipeline to Cloud Run..."
	python3 deploycloudrun.py

run:
	adk web .

web:
	adk web . --host 0.0.0.0

comic:
	cd ~/adkui/output
	python -m http.server 8000 --bind 0.0.0.0

agent1:
	adk web .
