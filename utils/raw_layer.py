class RawLayer:

    def __init__(self):
        pass

    def ingest_data_api(self, url):
        import pandas as pd 
        import requests
        from io import StringIO

        response = requests.get(url)

        if response.status_code == 200:
            data = response.text

            df = pd.read_csv(StringIO(data))

            # convert the dataframe to a csv in memory using StringIO
            csv_buffer = StringIO() #currently not a string but an object
            df.to_csv(csv_buffer, index=False)

            # getting the value from a particular object which is from csv_buffer
            return csv_buffer.getvalue()
        
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")



    def upload_data_to_s3(self, bucket_name, object_key, data):
        import os
        from dotenv import load_dotenv
        import boto3

        load_dotenv()

        aws_access_key_id = os.environ.get("aws_access_key_id")
        aws_secret_access_key = os.environ.get("aws_secret_access_key")

        s3_client = boto3.client(
            's3',
            region_name='ap-southeast-1',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        # upload data to s3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=data
        )

        return f"Data uploaded to S3 bucket '{bucket_name}' with object key '{object_key}'"


if __name__ == "__main__":
    obj = RawLayer()
    data = obj.ingest_data_api('https://raw.githubusercontent.com/jasmininnaka24/de_ecom_proj/refs/heads/main/data/Ecommerce_Order_Extract.csv')
    result = obj.upload_data_to_s3(
        'ecommercebucketdeproj',
        'raw/Ecommerce_Order_Extract.csv',
        data
    )
