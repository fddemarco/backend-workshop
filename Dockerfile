FROM python:3.10.16-bookworm

WORKDIR /usr/src/app

COPY ./dist/snaps-0.1.0-py3-none-any.whl ./dist/snaps-0.1.0-py3-none-any.whl
RUN pip install ./dist/snaps-0.1.0-py3-none-any.whl

COPY . .
EXPOSE 80
CMD ["fastapi", "run", "./src/snaps/main.py", "--port", "80"]
