def average(array):
    sets = set(array)
    liste = list(sets)
    return sum(liste) / len(liste)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)