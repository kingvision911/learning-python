fibonasi = []

def createFibo(limit: int):
    fibonasi.append(0)
    fibonasi.append(1)
    fibonasi.append(1)
    
    index = 2
    while fibonasi[index] < limit:
        fibonasi.append(fibonasi[index] + fibonasi[index-1])
        if fibonasi[index + 1] < limit:
            index = index + 1
        else:
            print(fibonasi[:-1])
            break
createFibo(100)

