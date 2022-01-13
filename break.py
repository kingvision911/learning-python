print('i will quit at 2\n')

for i in range(4):
    if i == 2:
        break
    print('i = %d\n' % i)

for i in range(4):
    if i == 2:
        continue
    print('i = %d\n' % i)
