from datetime import datetime, timedelta
from airflow.sdk import dag, task 
import os 
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.raw_layer import RawLayer

@dag(
    schedule='@daily',
    is_paused_upon_creation=False
)
def etl_ecom():

    @task.python(retries=3, retry_delay=timedelta(seconds=5))
    def extract_load_data():

        urls = [
            "https://raw.githubusercontent.com/jasmininnaka24/de_ecom_proj/refs/heads/main/data/Ecommerce_Order_Extract.csv"
        ]

        obj = RawLayer()
        for url in urls:
            fetched_data = obj.ingest_data_api(url)
            obj.upload_data_to_s3("ecommercebucketdeproj", f"raw/{url.split('/')[-1]}", fetched_data)

    
    extract_load_data = extract_load_data()
    extract_load_data

etl_ecom_dag_proj = etl_ecom()

