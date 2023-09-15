from itertools import product

A = input().split()
B = input().split()

A = [int(i) for i in A]
B = [int(i) for i in B]

liste = list(product(A,B))
print(*liste)
