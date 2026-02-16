# 3.1 Create and Access Tuple
print("---- 3.1 Create and Access ----")
tuple1 = (10, 20, 30, 40)

print("Tuple:", tuple1)

# Access elements
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])


# 3.2 Nested Tuple
print("\n---- 3.2 Nested Tuple ----")
nested_tuple = (1, 2, (3, 4, 5), 6)

print("Nested Tuple:", nested_tuple)
print("Access inner tuple:", nested_tuple[2])
print("Access element inside inner tuple:", nested_tuple[2][1])


# 3.3 Repetition of Tuple
print("\n---- 3.3 Repetition ----")
repeated_tuple = tuple1 * 2
print("Tuple after repetition:", repeated_tuple)


# 3.4 Concatenation of Tuples
print("\n---- 3.4 Concatenation ----")
tuple2 = (50, 60)
concatenated_tuple = tuple1 + tuple2

print("After concatenation:", concatenated_tuple)