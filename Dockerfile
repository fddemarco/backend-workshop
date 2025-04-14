# Stage 1: Base image with Python
FROM python:3.11-slim as base

# Install pip + poetry
RUN pip install --upgrade pip && pip install poetry

WORKDIR /app

# Copy wheel files and your built package
COPY wheels/ ./wheels/
COPY dist/your_package-*.whl ./dist/
COPY pyproject.toml poetry.lock ./

# Install from local wheels only
RUN pip install --no-index --find-links=./wheels your_package-*.whl

# Final stage: copy only what’s needed (optional)
FROM python:3.11-slim as final

COPY --from=base /usr/local /usr/local
COPY --from=base /app /app

CMD ["python", "-m", "your_package"]
