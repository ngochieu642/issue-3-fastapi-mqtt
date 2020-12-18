FROM python:3.7-stretch

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /code
COPY . /code

EXPOSE ${APP_PORT}

ENTRYPOINT [ "python", "/code/run.py"]