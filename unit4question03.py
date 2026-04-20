import json
import csv

# Step 1: Read JSON data from file
with open("data.json", "r") as json_file:
    data = json.load(json_file)   # JSON array (list of dictionaries)

# Step 2: Create CSV file
with open("output.csv", "w", newline="") as csv_file:
    # Extract headers from JSON keys
    headers = data[0].keys()
    
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()   # Write column names
    
    # Write data rows
    writer.writerows(data)

print("JSON data successfully converted to CSV!")