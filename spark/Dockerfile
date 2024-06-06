FROM bitnami/spark:3.2.1

USER root
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ /app/