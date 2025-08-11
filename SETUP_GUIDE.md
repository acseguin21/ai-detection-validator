# 🚀 Setup Guide for Cybersecurity Detection Framework

Congratulations! Your repository has been transformed into a professional, secure, and well-structured **Cybersecurity Detection Framework** that uses AI to improve detection rules. Here's everything you need to know to get started.

## 🎯 What We've Accomplished

### ✅ Project Structure
- **Professional directory layout** with `src/`, `tests/`, `config/`, and `docs/` folders
- **Comprehensive documentation** including README, security guidelines, and changelog
- **Security-first approach** with proper `.gitignore` and environment variable handling
- **Docker support** with multi-stage builds and containerization
- **CI/CD pipeline** with GitLab integration and security scanning

### ✅ Technology Migration
- **Switched from Vertex AI to Gemini AI** - much simpler setup!
- **API key authentication** instead of complex Google Cloud credentials
- **Updated dependencies** to use `google-generativeai` package
- **Enhanced security** with input validation and error handling
- **Cybersecurity focus** - specifically designed for detection rule improvement

## 🔑 Getting Your Gemini AI API Key

1. **Visit Google AI Studio**: Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. **Sign in** with your Google account
3. **Create API key**: Click "Create API Key" button
4. **Copy the key**: It will start with "AI" (e.g., `AIzaSyC...`)
5. **Keep it secure**: Never commit this key to version control!

## 🚀 Quick Start

### Option 1: Environment Variable (Recommended)
```bash
# Set your API key
export GEMINI_API_KEY="your-api-key-here"

# Run the script with example detection
python src/detection_test_script.py --yaml-file config/example_config.yml
```

### Option 2: .env File (Development)
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
echo "GEMINI_API_KEY=your-api-key-here" > .env

# Run the script
python src/detection_test_script.py --yaml-file config/example_config.yml
```

### Option 3: Command Line (Not recommended for production)
```bash
python src/detection_test_script.py --yaml-file config/example_config.yml --api-key "your-api-key"
```

## 🔒 Cybersecurity Detection Framework

### What It Does
This framework uses AI to provide **intelligent feedback** on your cybersecurity detection rules to:
- **Improve detection coverage** - Find more threats
- **Maximize true positives** - Reduce false alarms
- **Optimize Spark SQL queries** - Better performance in Databricks
- **Enhance rule titles** - More descriptive and actionable

### YAML Configuration Structure
Your detection configuration files should contain:

```yaml
title: "Detection Rule Title"
description: "What the detection is looking for"
sql_search: "Your Spark SQL query"
source_table: "Source log table name"
```

### Example Use Cases
- **PowerShell Detection**: Monitor for encoded commands
- **Brute Force Attacks**: Track failed login attempts
- **Data Exfiltration**: Monitor large data transfers
- **Lateral Movement**: Detect suspicious network activity

## 🛠️ Development Commands

The project includes a comprehensive Makefile for easy development:

```bash
# Show all available commands
make help

# Set up development environment
make quick-start

# Check your environment setup
make check-env

# Install dependencies
make install

# Run tests
make test

# Run linting and code quality checks
make lint

# Format code
make format

# Run security scans
make security

# Clean up temporary files
make clean

# Run with example configuration
make run-example
```

## 🐳 Docker Support

### Build and Run
```bash
# Build the image
make docker-build

# Run with Docker
make docker-run

# Run tests in Docker
make docker-test
```

### Docker Compose
```bash
# Development environment
docker-compose up

# Testing environment
docker-compose --profile testing up

# Production environment
docker-compose --profile production up
```

## 🔒 Security Features

- **API key validation** with format checking
- **Input sanitization** for YAML files
- **Secure error handling** (no sensitive info in error messages)
- **Environment variable management** (no hardcoded secrets)
- **Automated security scanning** in CI/CD pipeline
- **Container security** with non-root user execution

## 📁 Project Structure Explained

```
detection-ai-check-script/
├── src/                          # Source code
│   └── detection_test_script.py  # Main script (updated for cybersecurity)
├── config/                       # Detection configurations
│   ├── example_config.yml        # PowerShell detection example
│   ├── brute_force_detection.yml # Brute force attack detection
│   └── data_exfiltration.yml     # Data exfiltration detection
├── tests/                        # Test files
│   ├── __init__.py
│   ├── test_detection_script.py  # Unit tests
│   └── integration/              # Integration tests
│       └── test_integration.py
├── docs/                         # Documentation
│   └── SECURITY.md               # Security guidelines
├── requirements.txt               # Production dependencies
├── requirements-dev.txt           # Development dependencies
├── .gitignore                    # Git ignore rules
├── .gitlab-ci.yml                # CI/CD pipeline
├── Dockerfile                    # Docker configuration
├── docker-compose.yml            # Docker Compose setup
├── README.md                     # Project documentation
├── LICENSE                       # MIT license
├── CHANGELOG.md                  # Version history
├── Makefile                      # Development commands
├── setup.py                      # Package setup
├── .pre-commit-config.yaml       # Pre-commit hooks
└── .env.example                  # Environment variables template
```

## 🔄 Migration Summary

### What Changed
- **Authentication**: From complex Google Cloud credentials to simple API key
- **Dependencies**: From `google-cloud-aiplatform` to `google-generativeai`
- **Setup**: From `gcloud auth` to environment variable
- **Security**: Enhanced with input validation and secure error handling
- **Focus**: From general AI to cybersecurity detection improvement

### What Stayed the Same
- **YAML configuration** format (but with new fields)
- **Command-line interface** structure
- **Error handling** approach
- **Security features** and best practices

## 🚨 Important Security Notes

1. **Never commit your API key** to version control
2. **Use environment variables** or `.env` files for sensitive data
3. **The `.env` file is already in `.gitignore`** for security
4. **Rotate your API key** regularly
5. **Monitor usage** through Google AI Studio dashboard

## 🧪 Testing Your Setup

1. **Check environment**:
   ```bash
   make check-env
   ```

2. **Run tests**:
   ```bash
   make test
   ```

3. **Test with example detection**:
   ```bash
   make run-example
   ```

4. **Test different detection types**:
   ```bash
   # Test brute force detection
   python src/detection_test_script.py --yaml-file config/brute_force_detection.yml
   
   # Test data exfiltration detection
   python src/detection_test_script.py --yaml-file config/data_exfiltration.yml
   ```

## 📚 Next Steps

1. **Update your GitLab repository** with the new structure
2. **Set up CI/CD variables** in GitLab for your API key
3. **Customize the detection configurations** for your specific use cases
4. **Add your team members** and set up access controls
5. **Monitor the CI/CD pipeline** for security and quality checks
6. **Integrate with your Databricks environment** to implement improved detections

## 🆘 Need Help?

- **Documentation**: Check the `docs/` folder
- **Security**: Review `docs/SECURITY.md`
- **Issues**: Use GitLab Issues
- **Wiki**: Use GitLab Wiki for team documentation

---

**🎉 You're all set!** Your repository is now a professional, secure, and AI-powered **Cybersecurity Detection Framework** ready for production use with Gemini AI.
