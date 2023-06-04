# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /Server
ENV FLASK_APP=Servers/server_api.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV DB_URL=sql://lite
EXPOSE 5000
COPY . .
CMD ["flask", "run"]