x = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
y = [0.0 for i in range(6)]

for n, xn in enumerate(x):
    y[n] = xn ** 2

    print('n = %d, xn = %4.1f, and y[n] = %4.2f' % (n , xn , y[n]))

