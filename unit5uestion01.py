# Take filename from user
filename = input("Enter the filename: ")

try:
    # Try to open the file in read mode
    file = open(filename, "r")
    
    # Read and display content
    content = file.read()
    print("\nFile Content:\n")
    print(content)
    
    file.close()   # Properly close the file

# Handle file not found error
except FileNotFoundError:
    print("Error: The file does not exist.")

# Handle permission error
except PermissionError:
    print("Error: You do not have permission to read this file.")

# Handle any other unexpected errors
except Exception as e:
    print("An unexpected error occurred:", e)