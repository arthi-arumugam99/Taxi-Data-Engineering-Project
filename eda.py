import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = r"C:\Users\<name>\Desktop\Projects\Taxi Trip\pythonProject\cleaned_taxi_data.parquet"
df = pd.read_parquet(file_path)

# Basic Statistics
print("\nBasic Statistics:")
print(df[['trip_distance', 'trip_duration_minutes', 'total_amount', 'cost_per_mile']].describe())

# Distribution of Trip Distance
plt.figure(figsize=(8, 6))
plt.hist(df['trip_distance'], bins=50, range=(0, 20), alpha=0.7)
plt.title('Distribution of Trip Distances')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.show()

# Distribution of Trip Duration
plt.figure(figsize=(8, 6))
plt.hist(df['trip_duration_minutes'], bins=50, range=(0, 100), alpha=0.7)
plt.title('Distribution of Trip Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# Average Cost Per Mile
plt.figure(figsize=(8, 6))
plt.hist(df['cost_per_mile'], bins=50, range=(0, 30), alpha=0.7)
plt.title('Distribution of Cost Per Mile')
plt.xlabel('Cost Per Mile ($)')
plt.ylabel('Frequency')
plt.show()

# Most Frequent Pickup Locations
top_pickup_locations = df['PULocationID'].value_counts().head(10)
print("\nTop 10 Pickup Locations:")
print(top_pickup_locations)

# Visualization: Top 10 Pickup Locations
plt.figure(figsize=(8, 6))
top_pickup_locations.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Top 10 Pickup Locations')
plt.xlabel('Pickup Location ID')
plt.ylabel('Frequency')
plt.show()
