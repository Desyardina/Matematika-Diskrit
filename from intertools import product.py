 = {1, 2,A 3, 4}
B = {3, 4, 5, 6}
U = set(range(1, 9))

print("union            :", A | B)
print("Intersection     :", A & B)
print("Difference       :", A - B)
print("Complement       :", U - B)
print("Cardinality      :", len(A)) 
print("Subset?          :", A <= U)
print("A x B            :", set(product(A, B)))
