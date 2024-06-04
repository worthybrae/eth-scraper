from pyspark.sql import SparkSession
import json


def process_ethereumn_data():
    spark = SparkSession.builder.appName('Ethereum Processor').getOrCreate()
    df = spark.read.json("app/data/transactions.json")
    df.show()

if __name__ == '__main__':
    process_ethereumn_data()