#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# azure/deploy.sh — First-time Azure Resource Setup
#
# Run this ONCE manually to bootstrap Azure resources.
# After this, GitHub Actions handles all subsequent deployments.
#
# Prerequisites:
#   - Azure CLI installed and logged in (az login)
#   - Contributor role on the target subscription
#
# Usage:
#   chmod +x azure/deploy.sh
#   ./azure/deploy.sh
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

# ── Configuration (edit these) ───────────────────────────────────────────────
APP_NAME="ragrag"
RESOURCE_GROUP="rg-${APP_NAME}-prod"
LOCATION="southeastasia"
ACR_NAME="${APP_NAME}acr"          # Must be globally unique, alphanumeric only
SUBSCRIPTION_ID=$(az account show --query id -o tsv)

echo "============================================================"
echo "  AI-RAGSystem — Azure Bootstrap Setup"
echo "============================================================"
echo "  App Name      : $APP_NAME"
echo "  Resource Group: $RESOURCE_GROUP"
echo "  Location      : $LOCATION"
echo "  ACR Name      : $ACR_NAME"
echo "  Subscription  : $SUBSCRIPTION_ID"
echo "------------------------------------------------------------"
read -p "  Proceed? [y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

# ── 1. Create Resource Group ─────────────────────────────────────────────────
echo ""
echo "[1/5] Creating Resource Group..."
az group create \
    --name "$RESOURCE_GROUP" \
    --location "$LOCATION" \
    --output table

# ── 2. Create Azure Container Registry ───────────────────────────────────────
echo ""
echo "[2/5] Creating Azure Container Registry ($ACR_NAME)..."
az acr create \
    --resource-group "$RESOURCE_GROUP" \
    --name "$ACR_NAME" \
    --sku Basic \
    --admin-enabled true \
    --output table

# Get ACR credentials
ACR_LOGIN_SERVER=$(az acr show --name "$ACR_NAME" --query loginServer -o tsv)
ACR_USERNAME=$(az acr credential show --name "$ACR_NAME" --query username -o tsv)
ACR_PASSWORD=$(az acr credential show --name "$ACR_NAME" --query "passwords[0].value" -o tsv)

echo "  ACR Login Server: $ACR_LOGIN_SERVER"

# ── 3. Register Container Apps provider ─────────────────────────────────────
echo ""
echo "[3/5] Registering Azure providers..."
az provider register --namespace Microsoft.App --wait
az provider register --namespace Microsoft.OperationalInsights --wait
echo "  Providers registered."

# ── 4. Create Service Principal for GitHub Actions ───────────────────────────
echo ""
echo "[4/5] Creating Service Principal for GitHub Actions CI/CD..."
SP_NAME="sp-github-${APP_NAME}"
SP_JSON=$(az ad sp create-for-rbac \
    --name "$SP_NAME" \
    --role Contributor \
    --scopes "/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${RESOURCE_GROUP}" \
    --sdk-auth \
    --output json)

echo ""
echo "============================================================"
echo "  ✅ AZURE_CREDENTIALS (add this to GitHub Secrets):"
echo "------------------------------------------------------------"
echo "$SP_JSON"
echo "============================================================"
echo ""

# ── 5. Initial Bicep deployment (skeleton — no containers yet) ───────────────
echo "[5/5] Initial Bicep deployment (will be updated by CI/CD)..."
echo "  NOTE: Skipping first deploy — CI/CD will handle it on first push."
echo "        To deploy manually, run:"
echo ""
echo "  az deployment group create \\"
echo "    --resource-group $RESOURCE_GROUP \\"
echo "    --template-file azure/container-apps.bicep \\"
echo "    --parameters \\"
echo "      appName=$APP_NAME \\"
echo "      acrLoginServer=$ACR_LOGIN_SERVER \\"
echo "      acrUsername=$ACR_USERNAME \\"
echo "      acrPassword='$ACR_PASSWORD' \\"
echo "      geminiApiKey='<YOUR_GEMINI_KEY>' \\"
echo "      qdrantUrl='<YOUR_QDRANT_URL>' \\"
echo "      qdrantApiKey='<YOUR_QDRANT_KEY>' \\"
echo "      cloudAmqpUrl='<YOUR_CLOUDAMQP_URL>'"
echo ""

echo "============================================================"
echo "  ✅ Setup Complete!"
echo "------------------------------------------------------------"
echo "  Next steps:"
echo "  1. Add the AZURE_CREDENTIALS JSON above to GitHub Secrets"
echo "  2. Add the following secrets to GitHub:"
echo "     - AZURE_REGISTRY_LOGIN_SERVER = $ACR_LOGIN_SERVER"
echo "     - AZURE_REGISTRY_USERNAME     = $ACR_USERNAME"
echo "     - AZURE_REGISTRY_PASSWORD     = $ACR_PASSWORD"
echo "     - AZURE_RESOURCE_GROUP        = $RESOURCE_GROUP"
echo "     - AZURE_APP_NAME              = $APP_NAME"
echo "     - GEMINI_API_KEY              = <your key>"
echo "     - QDRANT_URL                  = <your qdrant url>"
echo "     - QDRANT_API_KEY              = <your qdrant key>"
echo "     - CLOUDAMQP_URL               = <your amqps:// url>"
echo "     - ALLOWED_ORIGINS             = https://your-app.azurecontainerapps.io"
echo "  3. Push to main branch to trigger CI/CD"
echo "============================================================"
