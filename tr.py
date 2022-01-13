# reversed() Demo
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5] # An input list of floats
y = [0.0 for i in range(6)] # A list filled using list comprehension
for n in reversed(range(len(x))):
    y[n] = x[n]**2 # without xn I have to access the list directly
    print('n = %d, xn = %4.1f, and y[n] = %4.2f' % (n, xn, y[n]))
