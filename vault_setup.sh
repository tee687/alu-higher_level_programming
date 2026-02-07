#!/usr/bin/env bash
# This script sets up a secure vault directory with keys, secrets, and logs
mkdir -p ~/secure_vault

echo "Welcome to the Keys Vault." > ~/secure_vault/keys.txt
echo "Welcome to the Secrets Vault." > ~/secure_vault/secrets.txt
echo "Welcome to the Logs Vault." > ~/secure_vault/logs.txt

echo "Vault Setup Complete!"
ls -l ~/secure_vault

