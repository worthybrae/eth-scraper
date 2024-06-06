from pyspark.sql import SparkSession
import json


def process_ethereum_data():
    spark = SparkSession.builder.appName('Ethereum Processor').getOrCreate()
    df = spark.read.json("app/data/transactions.json")
    df.show()

if __name__ == '__main__':
    process_ethereum_data()