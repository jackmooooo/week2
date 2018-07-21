import time

def search(array, input):
    for i in array:
        if i == input:
            print(i)

start = time.time()

search(range(0, 20000000000), 10000000000)

end = time.time()

print(end-start)
