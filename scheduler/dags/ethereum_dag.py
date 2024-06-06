from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from web3 import Web3
import json
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_ethereum_data():
    alchemy_url = f"https://eth-mainnet.g.alchemy.com/v2/{os.getenv('ALCHEMY_API_KEY')}"
    web3 = Web3(Web3.HTTPProvider(alchemy_url))
    block = web3.eth.get_block('latest')
    transactions = block.transactions

    with open('/opt/airflow/dags/data/transactions.json', 'w') as f:
        json.dump([web3.to_json(tx) for tx in transactions], f)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'ethereum_scraper',
    default_args=default_args,
    description='basic ethereum scraper dag',
    schedule_interval=timedelta(minutes=1)
)

fetch_task = PythonOperator(
    task_id = 'fetch_ethereum_data',
    python_callable=fetch_ethereum_data,
    dag=dag
)
