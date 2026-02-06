#!/bin/bash
PORT=${ISSUES_FS__UI__PORT:-10051}                                               # Default port 10041

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${SCRIPT_DIR}:${SCRIPT_DIR}/../Issues-FS:${SCRIPT_DIR}/../Issues-FS__Service:${PYTHONPATH}"

# Load environment variables from .env file if it exists
if [ -f .local-server.env ]; then
    echo "Loading environment variables from .local-server.env file..."
    export $(cat .local-server.env | grep -v '^#' | grep -v '^[[:space:]]*$' | xargs)
    echo "✓ Environment variables loaded"
else
    echo "⚠️  Warning: .local-server.env file not found"
    echo "   Create a .local-server.env file with your configuration"
    echo "   See local-server.env.example for available options"
fi

echo ""
echo "Issue Tracking Configuration:"
echo "  ISSUES_FS__UI__PORT = ${PORT}"
echo "  ISSUES__IN_MEMORY   = ${ISSUES__IN_MEMORY:-true (default)}"
echo "  ISSUES__PATH        = ${ISSUES__PATH:-.issues (default)}"
echo ""

poetry run uvicorn issues_fs_service_ui.fast_api.lambda_handler:app --reload --host 0.0.0.0 --port $PORT \
    --log-level info \
    --timeout-graceful-shutdown 0

#    --no-access-log  \