FROM python:3.11

WORKDIR /backend

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN apt-get update && apt-get install -y nano

COPY crm_yandex/ .

CMD ["gunicorn", "crm_yandex.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]
