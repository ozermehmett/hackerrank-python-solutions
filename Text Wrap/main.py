import textwrap


def wrap(string, max_width):
    word = list(string)

    satir = []
    line = ""

    for i in word:
        if len(line) < max_width:
            line += i
        else:
            satir.append(line)
            line = i
    satir.append(line)
    return "\n".join(satir)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)