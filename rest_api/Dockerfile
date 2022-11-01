FROM python:3.9.15-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["bash", "docker-entrypoint.sh"]
