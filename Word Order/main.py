n = int(input())
words = {}

for i in range(n):
    word = input()
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

print(len(words))
for word in words:
    print(words[word], end=' ')
