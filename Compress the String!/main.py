import itertools
n = input()
liste = []
for i in range(len(n)):
  liste.append(int(n[i]))
liste2 = [(len(list(g)), k) for k, g in itertools.groupby(liste)]
print(*liste2)
