FROM apache/airflow:2.3.0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /opt/airflow/dags/

COPY entrypoint.sh /entrypoint.sh

USER root
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]