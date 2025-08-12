#!/bin/bash
# Pre-commit hook to prevent committing secrets
# Author: Andre Seguin (acseguin21@gmail.com) - Calgary, Alberta, Canada 🇨🇦

echo "🔒 Running security checks before commit..."

# Check for potential API keys
if git diff --cached | grep -E "AIza[0-9A-Za-z_-]{35}" > /dev/null; then
    echo "❌ ERROR: Potential Google API key detected in staged changes!"
    echo "   Please remove any hardcoded API keys before committing."
    exit 1
fi

# Check for potential secrets
if git diff --cached | grep -E "(password|secret|token|key|credential).*=.*['\"][^'\"]{10,}" > /dev/null; then
    echo "❌ ERROR: Potential hardcoded secret detected in staged changes!"
    echo "   Please remove any hardcoded secrets before committing."
    exit 1
fi

# Check for .env files
if git diff --cached --name-only | grep -E "\.env" > /dev/null; then
    echo "❌ ERROR: .env file detected in staged changes!"
    echo "   Please remove .env files from staging area."
    exit 1
fi

# Check for credential files
if git diff --cached --name-only | grep -E "(credential|key|secret)" > /dev/null; then
    echo "⚠️  WARNING: Potential credential file detected in staged changes!"
    echo "   Please ensure this is not a real credential file."
    read -p "Continue with commit? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "✅ Security checks passed. Proceeding with commit..."
exit 0
