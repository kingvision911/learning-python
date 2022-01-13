x = [0, 0.1, 0.2, 0.3, 0.4, 0.5] # An input list of floats
y = [0.0 for i in range(6)]

for n in reversed(range(len(x))):
    y[n] = x[n] ** 2

    print('n = %d , xn = %4.2f, and y[n] = %4.2f' % (n , xn, y[n]))
