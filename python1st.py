# 1.1 Create and Access List Elements
print("---- 1.1 Create and Access ----")
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Access elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])


# 1.2 Add and Remove List Elements
print("\n---- 1.2 Add and Remove ----")

# Add elements
my_list.append(60)              # Add at end
print("After append(60):", my_list)

my_list.insert(2, 25)           # Insert at index 2
print("After insert(2,25):", my_list)

# Remove elements
my_list.remove(30)              # Remove specific value
print("After remove(30):", my_list)

my_list.pop()                   # Remove last element
print("After pop():", my_list)


# 1.3 Sort List Elements
print("\n---- 1.3 Sort ----")
my_list.sort()
print("Sorted List (Ascending):", my_list)

my_list.sort(reverse=True)
print("Sorted List (Descending):", my_list)


# 1.4 Reverse List Elements
print("\n---- 1.4 Reverse ----")
my_list.reverse()
print("Reversed List:", my_list)