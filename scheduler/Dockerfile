FROM apache/airflow:2.5.0


COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY dags/ /opt/airflow/dags/

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]


FROM apache/airflow:2.5.1

USER airflow

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY dags/ /opt/airflow/dags/

COPY entrypoint.sh /entrypoint.sh

USER root
RUN chmod +x /entrypoint.sh
RUN mkdir -p /opt/airflow/logs /opt/airflow/dags /opt/airflow/plugins
RUN chmod -R 755 /opt/airflow/logs /opt/airflow/dags /opt/airflow/plugins
RUN chown -R airflow: /opt/airflow/logs /opt/airflow/dags /opt/airflow/plugins

# Install any additional packages you need
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow
ENTRYPOINT ["/entrypoint.sh"]

