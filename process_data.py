from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, round

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Dataproc Taxi Data Processing") \
    .getOrCreate()

# Load the data from Google Cloud Storage
input_path = "gs://nyc-taxi-data-arthi/input-data/yellow_tripdata_2024-01.parquet"  # Your GCS path
print(f"Loading data from: {input_path}")
df = spark.read.parquet(input_path)

# Data Cleaning and Transformation
print("Performing data cleaning and transformations...")

# Convert datetime columns to timestamp
df = df.withColumn("tpep_pickup_datetime", to_timestamp(col("tpep_pickup_datetime"))) \
       .withColumn("tpep_dropoff_datetime", to_timestamp(col("tpep_dropoff_datetime")))

# Add a new column for trip duration in minutes
df = df.withColumn("trip_duration_minutes",
                   round((col("tpep_dropoff_datetime").cast("long") - col("tpep_pickup_datetime").cast("long")) / 60, 2))

# Filter out trips with invalid durations or distances
df = df.filter((col("trip_duration_minutes") > 0) & (col("trip_distance") > 0))

# Save the cleaned and processed data back to GCS
output_path = "gs://nyc-taxi-data-arthi/processed-data/cleaned_yellow_tripdata_2024-01.parquet"  # GCS output path
print(f"Saving processed data to: {output_path}")
df.write.mode("overwrite").parquet(output_path)

print("Data processing completed.")
