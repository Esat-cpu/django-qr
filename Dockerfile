FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential curl gettext \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN django-admin compilemessages

EXPOSE 8000

CMD ["gunicorn", "qryap.wsgi:application", "--bind", "0.0.0.0:8000"]
