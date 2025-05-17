#!/bin/bash
set -e

cd /app && alembic upgrade head
cd .. && uvicorn app.main:app --reload-dir app --host 0.0.0.0