# Define fuzzy sets
A = {'x1': 0.2, 'x2': 0.7, 'x3': 1.0}
B = {'x1': 0.5, 'x2': 0.4, 'x3': 0.8}

# Union
union = {x: max(A[x], B[x]) for x in A}

# Intersection
intersection = {x: min(A[x], B[x]) for x in A}

# Complement of A
complement_A = {x: 1 - A[x] for x in A}

# Difference A - B
difference = {x: min(A[x], 1 - B[x]) for x in A}

print("Union:", union)
print("Intersection:", intersection)
print("Complement of A:", complement_A)
print("Difference (A-B):", difference)

# Cartesian Product (Fuzzy Relation)
relation = {}
for x in A:
    for y in B:
        relation[(x, y)] = min(A[x], B[y])

print("\nFuzzy Relation (A x B):")
for k, v in relation.items():
    print(k, ":", v)

# Max-Min Composition
R = {
    ('x1', 'y1'): 0.2, ('x1', 'y2'): 0.7,
    ('x2', 'y1'): 0.5, ('x2', 'y2'): 0.4
}

S = {
    ('y1', 'z1'): 0.6, ('y1', 'z2'): 0.3,
    ('y2', 'z1'): 0.8, ('y2', 'z2'): 0.5
}

composition = {}

X = ['x1', 'x2']
Y = ['y1', 'y2']
Z = ['z1', 'z2']

for x in X:
    for z in Z:
        values = []
        for y in Y:
            values.append(min(R[(x, y)], S[(y, z)]))
        composition[(x, z)] = max(values)

print("\nMax-Min Composition:")
for k, v in composition.items():
    print(k, ":", v)