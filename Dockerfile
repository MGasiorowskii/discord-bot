FROM python:3.12-alpine
WORKDIR ./app
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app .
