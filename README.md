# Taxi Trip Data Engineering Project


## Project Overview: ##

This repository showcases a **Data Engineering workflow** for processing **yellow taxi trip data** from New York City. The pipeline utilizes **Google Cloud Platform** services, including **Google Cloud Dataproc**, **Google Cloud Storage (GCS)**, and **Google BigQuery** for storage and analysis. The data is processed using **Apache Spark**, a distributed data processing engine, which is run on **Google Cloud Dataproc**.


## Technologies Used: ##

- **Google Cloud Dataproc**: Dataproc was used to run the Spark jobs for data processing in a distributed manner across multiple nodes in the cloud.
- **Apache Spark**: Apache Spark was used for performing data transformations, cleaning, and filtering operations. It was run on **Google Dataproc** for distributed data processing.
- **GCS**: Google Cloud Storage was used to store both the raw taxi trip data (in Parquet format) and the processed data that was output by the Spark job. 
- **Google BigQuery:** BigQuery was used to load and analyze the processed taxi trip data. After data processing, the cleaned data was stored in **BigQuery** for querying and analysis.
- **Python and PySpark:** PySpark was used to write the data processing scripts that read data from **Google Cloud Storage**, transform it using **Apache Spark**, and then write the results back to **GCS**.


## Data Architecture: ##

![diagram-export-22-11-2024-04_48_52](https://github.com/user-attachments/assets/9775caf2-606a-4478-9343-45225a4ff684)



## Project Objectives: ## 

1. **Data Collection**:
   - The dataset consists of **yellow taxi trip data** from **New York City**. This dataset contains the following columns:
     - **VendorID**: An identifier for the vendor that provided the taxi.
     - **tpep_pickup_datetime**: The timestamp for when the trip started.
     - **tpep_dropoff_datetime**: The timestamp for when the trip ended.
     - **passenger_count**: The number of passengers in the trip.
     - **trip_distance**: The total distance traveled in miles.
     - **fare_amount**: The fare for the trip in USD.
     - **tip_amount**: The tip given to the driver.
   - The data is stored on **Google Cloud Storage** (GCS).

2. **Data Processing**:
   - The data is processed using **Apache Spark** running on **Google Cloud Dataproc**.
   - The script performs essential **data transformations** like handling null values, creating new calculated columns (e.g., `trip_duration_minutes`), and filtering invalid rows.

3. **Data Storage**:
   - After processing, the data is saved back to **Google Cloud Storage** (GCS) in Parquet format.

4. **Data Analysis**:
   - The processed data can be loaded into **Google BigQuery** for analysis.
   - BigQuery is used to run SQL queries and perform analytical tasks on the processed data.


## Project Flow

The project involves a sequence of steps from data collection to processing and finally loading into a data warehouse for analysis. Below are the detailed steps and workflow:

### **1. Data Collection**

The dataset used in this project is the **Yellow Taxi Trip Data** from **New York City**. This dataset is publicly available and contains trip details such as pickup/dropoff times, trip distance, fare amounts, etc. The data was stored in **Google Cloud Storage (GCS)** in **Parquet** format for efficient reading and storage.

### **2. Data Processing**

#### **Data Processing Goals**:
- **Data Cleaning**: Handle missing or null values, correct data types, and remove invalid data.
- **Data Transformation**: Create derived columns such as `trip_duration_minutes` and calculate other useful metrics.
- **Data Aggregation**: Aggregate data to derive insights like average fare or trip duration.

#### **Process**:
1. **Apache Spark** was used to process the data in a **distributed fashion** across multiple nodes in the **Dataproc cluster**.
2. The **PySpark** script performs the following tasks:
   - **Reading Data**: The data was read from the **Google Cloud Storage** bucket.
   - **Transformations**: Applied several transformations such as:
     - Converting pickup and dropoff times to timestamp format.
     - Creating a new column `trip_duration_minutes` by calculating the difference between pickup and dropoff times.
     - Filtering out invalid trips (e.g., trips with zero or negative duration).
   - **Data Cleansing**: Filling missing values in important columns like `passenger_count` with the median or other methods.
   - **Output**: The processed data is written back to **Google Cloud Storage** in **Parquet** format.


### **3. Job Submission to Dataproc:** <br>
Once the script was ready, it was uploaded to Google Cloud Storage (GCS) and submitted to the Dataproc cluster using the gcloud CLI:<br>

`gcloud dataproc jobs submit pyspark gs://nyc-taxi-data-arthi/scripts/process_data.py --cluster=taxi-data-cluster --region=us-central1 --async` <br>

This command triggers the PySpark job on the Dataproc cluster, where Spark processes the data in parallel across multiple worker nodes.

### **4. Loading Data into Google BigQuery:**
After processing, the cleaned data was saved back to Google Cloud Storage in Parquet format. It was then loaded into Google BigQuery for analysis.Once the data was loaded into BigQuery, I used SQL queries to perform some basic analysis, such as calculating average trip duration, fare amounts, etc.<br>

### **5. Visualisations:**

In this project, I used Python to visualise the processed yellow taxi trip data by connecting to Google BigQuery. Using libraries like Matplotlib and Pandas, I created various visualizations such as histograms to show the distribution of trip durations, scatter plots to explore the relationship between trip distance and fare amount, and bar charts to analyze the average tip amount by passenger count. These visualizations provided insights into patterns and trends in the data. Additionally, I connected Power BI to Google BigQuery to create interactive dashboards, where I could explore the data further with more advanced visualizations like trip counts, fare analysis, and tip distributions, helping to derive actionable insights from the data.<br>

![Screenshot 2024-11-22 045854](https://github.com/user-attachments/assets/0be1b39e-3af0-4f88-b1c7-6b8af4fbf898)


![Screenshot 2024-11-24 133901](https://github.com/user-attachments/assets/f9189221-38c0-429f-9b62-6895d0e64f2c)



## Challenges Faced: 
#### Quota Limitations:<br>
Initially, I ran into quota issues with SSD storage and network access. These were resolved by reducing the requested SSD storage and enabling Private Google Access on the subnetwork.
#### Spark Configuration:<br>
Ensuring the correct Java setup for Spark on Dataproc was a challenge but was resolved by configuring the cluster correctly.
#### Handling Large Datasets:<br>
Processing large datasets with Apache Spark on Dataproc required careful handling of memory and resource allocation.


The implementation is scalable and can be adapted to handle larger datasets or more complex transformations as required.

