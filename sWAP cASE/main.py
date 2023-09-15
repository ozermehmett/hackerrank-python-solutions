def swap_case(s):
    swapped = ''
    for c in s:
        if c.isupper():
            swapped += c.lower()
        else:
            swapped += c.upper()
    return swapped


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)