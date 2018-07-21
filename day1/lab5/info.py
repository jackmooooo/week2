def process(name):
    # name is a file, returns a list of strings
    #    from the file
    f = open(name)
    answer = []
    for line in f:
        answer.append(line.strip())
    return answer


if __name__ == '__main__':
    filename = "athletes.txt"
    data = process(filename)
    print("THE DATA IS:")
    for item in data:
        print(item)
    print()
