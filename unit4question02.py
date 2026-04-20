import csv

# Open the CSV file
with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    
    row_count = 0
    for row in reader:
        row_count += 1

print("Total number of rows:", row_count)