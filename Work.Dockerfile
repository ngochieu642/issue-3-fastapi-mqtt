FROM python:3.7-stretch

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY . /code
WORKDIR /code/app

EXPOSE 8000

ENTRYPOINT uvicorn main:app --reload