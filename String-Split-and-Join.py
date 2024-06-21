def split_and_join(line):
    str1 = line.split()
    joined_str = "-".join(str1)
    return joined_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
