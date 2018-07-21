def sorter(array):
    i = 1
    while i < len(array):
        num = array[i]
        x = i-1
        print("a " + str(array))
        while x < len(array):
            print("b " + str(array))
            if !(i == x) & num > array[x]:
                print("c " + str(array))
                array.insert(x+1, num)
                del array[1]
                x = len(array)
            x += 1
        i += 1
    print(array)

sorter([-2, 1, -3, 100])
