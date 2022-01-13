fibo = []

def createFibo(limit: int):
    fibo.append(0)
    fibo.append(1)
    fibo.append(1)

    index = 2
    while fibo[index] < limit:
        fibo.append(fibo[index] + fibo[index-1])
        if fibo[index + 1] < limit:
            index = index + 1
        else:
            print(fibo[:-1])
            break
createFibo(100)
