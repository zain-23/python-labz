collection = {1, 2, 5, 3, 4}
# print(type(collection))
collection.add(6) # None
# print(collection) # {1, 2, 3, 4, 5, 6}

# How to create empty set
sett = set()

# Union // Combine two sets and return a new set with all unique elements
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# print(set1.union(set2))

# Intersection // Find common elements between two sets and return a new set with common elements
set3 = {1,2,3}
set4 = {3,4,1}
# print(set3.intersection(set4))

# How many classroom is required for these students
subjects = {"Python","Java","Python","Python","Java","Java","C++","C++","C","Javascript"}
# print(len(subjects))

# Find out the way how save 9 and 9.0 in set
set6 = {
    ("int",9),
    ("float",9.0),
}
print(set6)