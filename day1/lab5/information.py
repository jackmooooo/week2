def process(name):
    f = open(name)
    answer = []
    for i in f:
        answer.append(i[:-1].split(":"))
    return answer

def average(arr):
    x = 0
    for i in arr:
        x += i
    return x/(len(array))

def rangeh(arr):
    highest = 0
    lowest = arr[0]
    for num in arr:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    return [lowest, highest]

def ambt6ftn6ft6in(arr):
    answer = 0
    for num in arr:
        if num <= 78 & num >= 72:
            answer += 1
        else:
            i_done_it = "banana"
    return answer
def amex6ft2in(arr):
    answer = 0
    for num in arr:
        if num == 74:
            answer += 1
    return answer

def group(info, gender, sport):
    ammount = 0
    for line in info:
        if line[2] == gender:
            if line[3] == sport:
                ammout += 1
            else:
                banana = "banana"
        else:
            banana = "banana+"
    return ammount


if __name__ == '__main__':
    filename = "athletes.txt"
    array = []
    data = process(filename)
    print("THE DATA IS:")
    for item in data:
        print(item)
        array.append(int(item[4]))
    print ("")
    print("the average height is " + str(average(array)))
    print("the range of heights is " + ((str(rangeh(array)).replace(", ", " to ")).replace("[", "")).replace("]", ""))
    print("the ammout on people between 6 feet and 6 feet 6 inches is " + str(ambt6ftn6ft6in(array)))
    print("the amount of people who are exacly 6 feet 2 inches is " + str(amex6ft2in(array)))
    morf = input("male of female?  >> ")
    sport = input("what sport?  >> ")
    print("the ammount of people in who are " + morf + " and are in " + sport + " is " + str(group(data, morf, sport)))
