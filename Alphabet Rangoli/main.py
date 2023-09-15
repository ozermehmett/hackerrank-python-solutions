def print_rangoli(size):
    n = size
    m = size * 4 - 3
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    rangoli = []
    for i in range(n):
        s = "-".join(alfabe[i:n])
        rangoli.append((s[::-1] + s[1:]).center(m, "-"))
    print('\n'.join(rangoli[:0:-1] + rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)