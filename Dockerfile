FROM python:3.10-slim-bookworm AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
ADD . /app
RUN uv build --out-dir /dist

FROM python:3.10-slim-bookworm
WORKDIR /app
COPY --from=builder /dist /dist
RUN pip install /dist/*.whl
COPY --from=builder /app/src /app/src
EXPOSE 80
CMD ["fastapi", "run", "/app/src/snaps/main.py", "--port", "80"]
