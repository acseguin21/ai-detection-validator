# AI Detection Validator

> **AI-powered cybersecurity detection validation framework for improving detection coverage and quality**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)

## 🎯 **Overview**

The AI Detection Validator is a professional cybersecurity tool that leverages Google Gemini AI to provide intelligent feedback on cybersecurity detection rules. Designed specifically for security engineers working with Spark SQL in Databricks environments, this framework helps maximize true positive outcomes while reducing false positives.

## ✨ **Key Features**

- **🤖 AI-Powered Feedback**: Get intelligent suggestions from Google Gemini AI for detection improvement
- **🔒 Cybersecurity Focused**: Specifically designed for cyber datalake detection rules
- **🐳 Docker Ready**: Full containerization with Docker and Docker Compose support
- **📊 Structured Output**: Professional, formatted feedback with actionable insights
- **⚡ Easy Testing**: One-command deployment with `docker-compose up`
- **🔐 Security First**: Secure API key management and non-root container execution

## 🚀 **Quick Start**

### **Prerequisites**
- Docker and Docker Compose
- Google Gemini AI API key ([Get one here](https://makersuite.google.com/app/apikey))

### **1. Clone the Repository**
```bash
git clone https://github.com/acseguin21/ai-detection-validator.git
cd ai-detection-validator
```

### **2. Configure Environment**
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### **3. Run with Docker Compose**
```bash
docker-compose up app
```

## 📋 **Usage Examples**

### **Test PowerShell Detection**
```bash
DETECTION_CONFIG=example_config.yml docker-compose up app
```

### **Test Brute Force Detection**
```bash
DETECTION_CONFIG=brute_force_detection.yml docker-compose up app
```

### **Test Data Exfiltration Detection**
```bash
DETECTION_CONFIG=data_exfiltration.yml docker-compose up app
```

## 🏗️ **Architecture**

- **Frontend**: Command-line interface with professional output formatting
- **Backend**: Python-based detection validation engine
- **AI Integration**: Google Gemini AI for intelligent feedback generation
- **Containerization**: Multi-stage Docker builds for development and production
- **Security**: Non-root execution, secure environment variable handling

## 🔧 **Development**

### **Local Development**
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
make test

# Run locally
python src/detection_test_script.py --yaml-file config/example_config.yml --api-key YOUR_API_KEY
```

### **Docker Development**
```bash
# Build image
make docker-build

# Run tests in container
make docker-test

# Run with custom config
DETECTION_CONFIG=brute_force_detection.yml docker-compose up app
```

## 📁 **Project Structure**

```
ai-detection-validator/
├── src/                    # Source code
│   └── detection_test_script.py
├── config/                 # Detection configurations
│   ├── example_config.yml
│   ├── brute_force_detection.yml
│   └── data_exfiltration.yml
├── tests/                  # Test suite
├── docs/                   # Documentation
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # Multi-stage Docker build
└── requirements.txt       # Python dependencies
```

## 🛡️ **Security Features**

- **Non-root container execution**
- **Secure API key management**
- **Input validation and sanitization**
- **Automated security scanning**
- **Pre-commit security hooks**

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- Google Gemini AI for providing the AI capabilities
- The cybersecurity community for feedback and testing
- Open source contributors who made this project possible

---

**Built with ❤️ for the cybersecurity community**
