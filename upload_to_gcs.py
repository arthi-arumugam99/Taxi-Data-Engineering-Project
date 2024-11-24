from google.cloud import storage
import os

# Set the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\arthi\Downloads\taxi-data-uploader-dda781791376.json"


def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    """
    Uploads a file to Google Cloud Storage.

    :param bucket_name: Name of the GCS bucket.
    :param source_file_path: Local path to the file to upload.
    :param destination_blob_name: Destination path in the GCS bucket.
    """
    # Initialize GCS client
    storage_client = storage.Client()


    bucket = storage_client.bucket(bucket_name)
    if not bucket.exists():
        print(f"Bucket {bucket_name} does not exist.")
        return

    # Create a blob and upload the file
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)
    print(f"File {source_file_path} uploaded to {bucket_name}/{destination_blob_name}.")


# GCS bucket name and file details
bucket_name = "nyc-taxi-data-arthi"  
source_file_path = r"C:\Users\arthi\Desktop\Projects\Taxi Trip\data\yellow_tripdata_2024-01.parquet"
destination_blob_name = "processed_data/yellow_tripdata_2024-01.parquet"

# Upload the file
upload_to_gcs(bucket_name, source_file_path, destination_blob_name)
