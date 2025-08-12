# Security Guidelines

This document outlines the security measures and best practices for the Detection AI Check Script project.

**Project Maintainer**: Andre Seguin (acseguin21@gmail.com) - Calgary, Alberta, Canada 🇨🇦

## 🔐 API Key Security

### Gemini AI API Key Management

**CRITICAL**: Never commit your Gemini AI API key to version control!

1. **Get your API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key (it starts with "AI")

2. **Set up your API key securely**:
   ```bash
   # Option 1: Environment variable (recommended)
   export GEMINI_API_KEY="your-api-key-here"
   
   # Option 2: .env file (for development only)
   echo "GEMINI_API_KEY=your-api-key-here" > .env
   
   # Option 3: Command line (not recommended for production)
   python script.py --api-key "your-api-key-here"
   ```

3. **Verify your .env file is ignored**:
   - Check that `.env` is in your `.gitignore` file
   - Never commit `.env` files to version control

### Environment Variable Security

- Use environment variables for all sensitive configuration
- Never hardcode API keys, passwords, or tokens in source code
- Use `.env.example` files to document required environment variables
- Rotate API keys regularly

## 🛡️ Input Validation

### YAML File Security

- All YAML files are parsed using `yaml.safe_load()` to prevent code execution
- Input files are validated for required fields
- File paths are sanitized to prevent directory traversal attacks

### Command Line Arguments

- All command line arguments are validated
- File paths are checked for existence before processing
- API keys are validated for proper format

## 🔒 Error Handling

### Information Disclosure Prevention

- Error messages do not reveal sensitive information
- Stack traces are not exposed in production
- Generic error messages for authentication failures
- No internal system information in error responses

### Secure Logging

- No sensitive data in log files
- Log levels appropriate for production environments
- Structured logging for better security monitoring

## 🐳 Container Security

### Docker Security Best Practices

- Multi-stage builds to reduce attack surface
- Non-root user execution
- Minimal base images
- Regular security updates
- Health checks for monitoring

### Runtime Security

- Read-only file systems where possible
- Network isolation
- Resource limits
- Security scanning with Trivy

## 🔍 Security Scanning

### Automated Security Checks

The CI/CD pipeline includes:

1. **Bandit**: Python security linter
2. **Safety**: Dependency vulnerability scanning
3. **Trivy**: Container image vulnerability scanning
4. **Custom compliance checks**: Hardcoded secrets detection

### Running Security Scans Locally

```bash
# Install security tools
pip install -r requirements-dev.txt

# Run security scans
bandit -r src/
safety check
```

## 🚨 Incident Response

### Security Vulnerability Reporting

If you discover a security vulnerability:

1. **DO NOT** create a public issue
2. Email [security@yourdomain.com] with details
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment
   - Suggested fix (if available)

### Response Timeline

- **Critical vulnerabilities**: 24-48 hours
- **High severity**: 1 week
- **Medium severity**: 2 weeks
- **Low severity**: 1 month

## 🔐 Access Control

### Repository Access

- Use GitLab's role-based access control
- Require code review for all changes
- Protect main branch with merge request requirements
- Use signed commits for critical changes

### Deployment Access

- Separate credentials for different environments
- Use GitLab CI/CD variables for sensitive data
- Implement least privilege principle
- Regular access reviews

## 📋 Security Checklist

Before deploying to production:

- [ ] API keys are set via environment variables
- [ ] No hardcoded secrets in source code
- [ ] All dependencies are up to date
- [ ] Security scans pass
- [ ] Error handling prevents information disclosure
- [ ] Input validation is implemented
- [ ] Container security best practices followed
- [ ] Access controls are properly configured

## 🆘 Security Contacts

- **Security Team**: [security@yourdomain.com]
- **Emergency**: [emergency@yourdomain.com]
- **Bug Bounty**: [bounty@yourdomain.com]

## 📚 Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [Python Security Best Practices](https://python-security.readthedocs.io/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
