# =============================================================================
# AI Detection Validator - Makefile
# 
# Author: Andre Seguin (acseguin21@gmail.com)
# Location: Calgary, Alberta, Canada 🇨🇦
# 
# This Makefile provides common development and deployment commands
# for the AI Detection Validator project.
# =============================================================================

.PHONY: help install test lint format security clean docker-build docker-run docker-test deploy

# Default target
help:
	@echo "Available commands:"
	@echo "  install         - Install dependencies"
	@echo "  test            - Run tests"
	@echo "  lint            - Run linting and code quality checks"
	@echo "  format          - Format code with black and isort"
	@echo "  security        - Run security scans (bandit, safety)"
	@echo "  security-scan   - Run comprehensive security check (includes secret detection)"
	@echo "  clean           - Clean up temporary files"
	@echo "  docker-build    - Build Docker image"
	@echo "  docker-run      - Run Docker container"
	@echo "  docker-test     - Run tests in Docker"
	@echo "  deploy          - Deploy to production"

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# Run tests
test:
	@echo "Running tests..."
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

# Run linting and code quality checks
lint:
	@echo "Running linting checks..."
	black --check --diff src/ tests/
	isort --check-only --diff src/ tests/
	flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503
	mypy src/ --ignore-missing-imports

# Format code
format:
	@echo "Formatting code..."
	black src/ tests/
	isort src/ tests/

# Run security scans
security:
	@echo "Running security scans..."
	bandit -r src/ -f json -o bandit-report.json
	safety check --json --output safety-report.json
	@echo "Security scan reports generated: bandit-report.json, safety-report.json"

# Run comprehensive security check
security-scan:
	@echo "🔒 Running comprehensive security check..."
	@echo "Checking for hardcoded secrets..."
	@if [ -f "scripts/pre-commit-hook.sh" ]; then \
		echo "✅ Pre-commit hook found"; \
	else \
		echo "⚠️  Pre-commit hook not found"; \
	fi
	@echo "Checking for potential API keys..."
	@if grep -r "AIza[0-9A-Za-z_-]\{35\}" src/ tests/ 2>/dev/null; then \
		echo "❌ Potential API keys found in source code!"; \
		exit 1; \
	else \
		echo "✅ No potential API keys found in source code."; \
	fi
	@echo "Checking for hardcoded secrets..."
	@if grep -r "password.*=.*['\"][^'\"]\{10,\}" src/ tests/ 2>/dev/null; then \
		echo "❌ Potential hardcoded secrets found!"; \
		exit 1; \
	else \
		echo "✅ No potential hardcoded secrets found."; \
	fi
	@echo "Checking for test API keys..."
	@if grep -r "test_api_key_for_testing_purposes_only_12345" src/ tests/ 2>/dev/null; then \
		echo "✅ Test API keys found (this is expected)"; \
	else \
		echo "⚠️  No test API keys found"; \
	fi
	@echo "✅ Comprehensive security check completed!"

# Clean up temporary files
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type f -name "*.log" -delete
	rm -rf build/ dist/ .tox/ .mypy_cache/

# Build Docker image
docker-build:
	@echo "Building Docker image..."
	docker build -t detection-ai-script:latest .

# Run Docker container
docker-run:
	@echo "Running Docker container..."
	docker run --rm -it \
		-v $(PWD)/config:/app/config \
		-e GEMINI_API_KEY=$(GEMINI_API_KEY) \
		detection-ai-script:latest \
		python src/detection_test_script.py --yaml-file /app/config/example_config.yml

# Run tests in Docker
docker-test:
	@echo "Running tests in Docker..."
	docker run --rm -it \
		-v $(PWD)/src:/app/src \
		-v $(PWD)/tests:/app/tests \
		detection-ai-script:latest \
		pytest tests/ -v

# Deploy to production
deploy:
	@echo "Deploying to production..."
	@if [ -z "$(GEMINI_API_KEY)" ]; then \
		echo "Error: GEMINI_API_KEY environment variable not set"; \
		exit 1; \
	fi
	docker-compose --profile production up -d

# Development setup
dev-setup: install
	@echo "Setting up development environment..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env file from .env.example"; \
		echo "Please edit .env and add your GEMINI_API_KEY"; \
	else \
		echo ".env file already exists"; \
	fi

# Quick start
quick-start: dev-setup
	@echo "Quick start setup complete!"
	@echo "Next steps:"
	@echo "1. Edit .env and add your GEMINI_API_KEY"
	@echo "2. Create a config file in config/ directory"
	@echo "3. Run: python src/detection_test_script.py --yaml-file config/your_config.yml"

# Check environment
check-env:
	@echo "Checking environment..."
	@if [ -z "$(GEMINI_API_KEY)" ]; then \
		echo "❌ GEMINI_API_KEY not set"; \
	else \
		echo "✅ GEMINI_API_KEY is set"; \
	fi
	@if [ -f .env ]; then \
		echo "✅ .env file exists"; \
	else \
		echo "❌ .env file missing"; \
	fi
	@if [ -f config/example_config.yml ]; then \
		echo "✅ Example config exists"; \
	else \
		echo "❌ Example config missing"; \
	fi

# Run with example config
run-example:
	@echo "Running with example configuration..."
	@if [ -z "$(GEMINI_API_KEY)" ]; then \
		echo "Error: GEMINI_API_KEY environment variable not set"; \
		echo "Please set it first: export GEMINI_API_KEY='your-api-key'"; \
		exit 1; \
	fi
	python src/detection_test_script.py --yaml-file config/example_config.yml
