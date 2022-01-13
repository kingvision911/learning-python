print('the program to add or append the value on the last position')
student = ['amos','julius', 'johnson', 'Brian', 'keneth']
student.append('morison')

print(student)

print('it removes the first value in the list\n')
listt = ['nano', 'sudo', 'arch', 'juma']
listt.pop(0)
print(listt)

print('clear all the value in the list\n')
names = ['japthogo','ubungo', 'router', 'japan']
names.clear()
print(names)

print('add the value in the spesific position\n')
imani = ['chakula', 'kulala', 'kusoma', 'kupika']
imani.insert(2, 'wsichana')
print(imani)
 
print('count chakula value in the list\n')
pearl = ['chakula','chakula', 'mchapakazi', 'mvivu', 'kucheza']
print(pearl)
print(pearl.count('chakula'))

print('find the index of the value in the list')
name = ['kazi', 'kupumzika', 'kucheza','kuruka']
print(name)
print(name.index('kucheza'))

print('return the shallow copy of the list')
cp = [1, 34, 3, 5, 0]
cpy = cp.copy()
print(cpy)

print('revese the list form back to front')
ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('using the other way')
ar.reverse()
print(ar)

res = ar[::-1]
print(res)

print('sorting the value')
lis = [3, 1, 6, 2, 4, 5]
lis.sort()
print(lis)
