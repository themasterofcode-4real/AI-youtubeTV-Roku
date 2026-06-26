# Placeholder Dockerfile for the future backend service.
# Phase 2 intentionally does not build or run an application.
FROM python:3.13-slim AS skeleton

WORKDIR /app
COPY pyproject.toml README.md ./
COPY backend ./backend

CMD ["python", "-c", "print('AI TV Assistant skeleton: no runnable service in Phase 2')"]
