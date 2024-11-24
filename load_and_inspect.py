import requests
import os

# URL for the NYC Taxi dataset
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-02.parquet"

# Local directory to save the downloaded file
local_dir = r"C:\Users\<name>\Desktop\Projects\Taxi Trip\pythonProject\data"
os.makedirs(local_dir, exist_ok=True)  

# Local file path
local_file_path = os.path.join(local_dir, "yellow_tripdata_2024-02.parquet")

# Download the file
print(f"Downloading data from {url}...")
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(local_file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File downloaded successfully and saved to {local_file_path}")
else:
    print(f"Failed to download data. HTTP Status Code: {response.status_code}")
