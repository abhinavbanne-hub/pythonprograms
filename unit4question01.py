# Step 1: Writing to a file (creates file if it doesn't exist)
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("File handling in Python is easy.\n")
file.close()   # Closing file

# Step 2: Reading the file
file = open("sample.txt", "r")
content = file.read()
print("File Content After Writing:\n", content)
file.close()   # Closing file

# Step 3: Appending new content
file = open("sample.txt", "a")
file.write("This line is added later.\n")
file.close()   # Closing file

# Step 4: Reading again after appending
file = open("sample.txt", "r")
content = file.read()
print("File Content After Appending:\n", content)
file.close()   # Closing file