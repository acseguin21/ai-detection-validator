# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Project Maintainer**: Andre Seguin (acseguin21@gmail.com) - Calgary, Alberta, Canada 🇨🇦

## [Unreleased]

### Added
- Initial project structure
- Gemini AI integration
- YAML configuration support
- Comprehensive testing suite
- Security scanning and validation
- Docker containerization
- GitLab CI/CD pipeline
- Development tools and Makefile

## [1.0.0] - 2024-01-XX

### Added
- Initial release of Detection AI Check Script
- Command-line interface for Gemini AI interactions
- YAML-based prompt configuration
- API key validation and security
- Error handling and user feedback
- Support for multiple Gemini models
- Environment variable configuration
- Comprehensive documentation

### Security
- API key validation and format checking
- Secure environment variable handling
- Input validation and sanitization
- No hardcoded secrets
- Comprehensive security documentation

### Development
- Full test coverage
- Code quality tools (black, flake8, isort, mypy)
- Security scanning (bandit, safety)
- Docker support with multi-stage builds
- GitLab CI/CD with security scanning
- Development environment setup scripts

## [0.2.0] - 2024-01-XX

### Changed
- Migrated from Vertex AI to Gemini AI
- Simplified authentication (API key only)
- Updated dependencies and requirements
- Enhanced error handling and validation

### Removed
- Google Cloud Platform dependencies
- Service account authentication
- Complex credential management

## [0.1.0] - 2024-01-XX

### Added
- Initial Vertex AI integration
- Basic command-line interface
- YAML configuration support
- Service account authentication

---

## Version History

- **1.0.0**: Production-ready release with Gemini AI
- **0.2.0**: Migration from Vertex AI to Gemini AI
- **0.1.0**: Initial prototype with Vertex AI

## Contributing

When contributing to this project, please update this changelog with your changes.
Follow the existing format and add entries under the [Unreleased] section.

### Changelog Entry Format

```
### Added
- New feature description

### Changed
- Changed feature description

### Deprecated
- Deprecated feature description

### Removed
- Removed feature description

### Fixed
- Bug fix description

### Security
- Security improvement description
```
