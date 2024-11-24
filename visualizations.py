import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = r"C:\Users\arthi\Desktop\Projects\Taxi Trip\pythonProject\cleaned_taxi_data.parquet"
df = pd.read_parquet(file_path)

# Distribution of Trip Distance
plt.figure(figsize=(8, 6))
plt.hist(df['trip_distance'], bins=50, range=(0, 20), alpha=0.7, color='blue')
plt.title('Distribution of Trip Distances')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Distribution of Trip Duration
plt.figure(figsize=(8, 6))
plt.hist(df['trip_duration_minutes'], bins=50, range=(0, 100), alpha=0.7, color='green')
plt.title('Distribution of Trip Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Distribution of Cost Per Mile
plt.figure(figsize=(8, 6))
plt.hist(df['cost_per_mile'], bins=50, range=(0, 30), alpha=0.7, color='orange')
plt.title('Distribution of Cost Per Mile')
plt.xlabel('Cost Per Mile ($)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Top 10 Pickup Locations
top_pickup_locations = df['PULocationID'].value_counts().head(10)
plt.figure(figsize=(8, 6))
top_pickup_locations.plot(kind='bar', color='purple', alpha=0.7)
plt.title('Top 10 Pickup Locations')
plt.xlabel('Pickup Location ID')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()
