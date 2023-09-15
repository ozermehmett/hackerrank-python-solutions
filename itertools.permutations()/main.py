from itertools import permutations
a, l = input().split()
l = int(l)

perms = list(permutations(a, l))
perms = sorted(perms)
for perm in perms:
    print(''.join(perm))
