

def split_and_join(line):
    word = line.split(" ")
    new = "-".join(word)
    return new
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
