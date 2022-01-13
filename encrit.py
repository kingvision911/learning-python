converted = input('Enter the sentence you want to encript or decript: \n')

language = ''
i =len(converted) - 1

while i >= 0:

   language = language + converted[i]
    print(i, converted[i] , language)
    i = i - 1

print(language)

