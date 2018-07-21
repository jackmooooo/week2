import time

def F(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n*F(n-1)

def f(n):
    answer = 1
    x = 1
    while x < n:
        answer = answer * x
        x += 1
    return answer

start = time.time()

def tosci(n):
    a = (str(n).split("")).insert(".", 1)
    b = a[12:]
    return str(b)+" x 10^"+str(len(a[:12]))


print(tosci(f(100000)))

end = time.time()

print((end-start)/60000)
