n, m = input().split()
arr = input().split()
set_a = set(input().split())
set_b = set(input().split())

happiness = 0

for i in arr:
    if i in set_a:
        happiness += 1
    elif i in set_b:
        happiness -= 1

print(happiness)
