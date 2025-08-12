# =============================================================================
# AI Detection Validator - Dockerfile
# 
# Author: Andre Seguin (acseguin21@gmail.com)
# Location: Calgary, Alberta, Canada 🇨🇦
# 
# Multi-stage Docker build for the AI Detection Validator project
# Includes development, testing, and production stages
# =============================================================================

# Use official Python runtime as base image
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        libffi-dev \
        libssl-dev \
        curl \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY config/ ./config/

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Default command
CMD ["python", "src/detection_test_script.py", "--help"]

# Production stage
FROM base as production

# Switch back to root for package removal
USER root

# Remove development dependencies
RUN apt-get update \
    && apt-get remove -y gcc g++ \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Switch back to non-root user
USER appuser

# Development stage
FROM base as development

# Switch back to root for development dependencies
USER root

# Install development dependencies
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Switch back to non-root user
USER appuser

# Testing stage
FROM development as testing

# Copy test files
COPY tests/ ./tests/

# Run tests by default
CMD ["pytest", "tests/", "-v"]
