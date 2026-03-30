# 2.1 Create and Access Set Elements
print("---- 2.1 Create and Access ----")
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

# Accessing elements (using loop because sets are unordered)
print("Elements in Set 1:")
for element in set1:
    print(element)


# 2.2 Union of Elements
print("\n---- 2.2 Union ----")
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)


# 2.3 Intersection of Elements
print("\n---- 2.3 Intersection ----")
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)


# 2.4 Difference of Elements
print("\n---- 2.4 Difference ----")
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)
