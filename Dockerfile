FROM python:3.9-slim

RUN apt-get update && apt-get install -y wget unzip curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN mkdir -p /app/templates /app/static

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]