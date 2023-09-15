def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i))[2:]
        hexa = str(hex(i))[2:]
        binary = str(bin(i))[2:]
        print(decimal.rjust(width), octal.rjust(width), hexa.upper().rjust(width), binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)