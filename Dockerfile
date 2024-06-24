FROM python:3.12-alpine
WORKDIR ./app
ENV PYTHONUNBUFFERED 1
COPY ./Pipfile* .
RUN python -m pip install --upgrade pip &&  \
    pip install pipenv &&  \
    pipenv install --dev --system --deploy
COPY ./app .
CMD ["python", "main.py"]
