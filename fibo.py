fibo = []

def tengenezaFibo(mia: int):
    fibo.append(0)
    fibo.append(3)
    fibo.append(5)

    index = 2
    while fibo[index] < mia:
        fibo.append(fibo[index] + 2)
        if fibo[index + 1] < mia:
            index = index + 1
        else:
            print(fibo[:-1])
            break
tengenezaFibo(20)
