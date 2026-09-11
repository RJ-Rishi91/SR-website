#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR/backend"

if [ -d "venv" ]; then
    source venv/bin/activate
fi

export PYTHONPATH=.
echo "Starting Studio Ravya FastAPI backend on http://localhost:8000..."
exec python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
