# 4.1 Create and Access Dictionary Elements
print("---- 4.1 Create and Access ----")
student = {
    "name": "Rahul",
    "age": 20,
    "course": "B.Tech"
}

print("Dictionary:", student)

# Access elements
print("Name:", student["name"])
print("Age:", student.get("age"))


# 4.2 Update Dictionary
print("\n---- 4.2 Update Dictionary ----")

# Update existing key
student["age"] = 21

# Add new key-value pair
student["grade"] = "A"

print("After Update:", student)


# 4.3 Removing Elements
print("\n---- 4.3 Removing Elements ----")

# Remove specific key
student.pop("course")
print("After pop('course'):", student)

# Remove last inserted item
student.popitem()
print("After popitem():", student)


# 4.4 Merging Dictionaries
print("\n---- 4.4 Merging Dictionaries ----")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: update()
dict1.update(dict2)
print("After Merging using update():", dict1)

# Method 2: Using | operator (Python 3.9+)
merged_dict = dict1 | dict2
print("After Merging using | operator:", merged_dict)