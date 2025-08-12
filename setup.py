#!/usr/bin/env python3
"""
Setup script for Detection AI Check Script
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="detection-ai-check-script",
    version="1.0.0",
    author="Andre Seguin",
    author_email="acseguin21@gmail.com",
    description="A secure Python application for interacting with Google Gemini AI",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/acseguin21/ai-detection-validator",
    project_urls={
        "Bug Tracker": "https://github.com/acseguin21/ai-detection-validator/issues",
        "Documentation": "https://github.com/acseguin21/ai-detection-validator",
        "Source Code": "https://github.com/acseguin21/ai-detection-validator",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.11.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            "mypy>=1.5.0",
            "bandit>=1.7.5",
            "safety>=2.3.0",
            "pre-commit>=3.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "detection-ai=detection_test_script:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="ai, gemini, google, yaml, cli, security",
)
