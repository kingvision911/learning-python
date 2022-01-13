import math, pyperclip 

def main():
    print('After encrypting\n') 
    mymessage = 'common sense is not so common'
    mykey = 8

    ciphertext = encryptMessage(mykey, mymessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):

            ciphertext[col] += message[pointer]
            pointer += key 

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()

#this code is for the decrhyption program

def main():
    print('After decrypting\n')
    mymessage = 'cenoonommstmme oo snnio s s c'
    mykey = 8

    plaintext = decryptMessage(mykey, mymessage)

    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    numofcol = math.ceil(len(message) / key)

    numofrow = key

    numofshadedbox = (numofrow * numofcol) - len(message)
    
    plaintext = [''] * numofcol
    
    col = 0
    row = 0

    for symbol in message:

        plaintext[col] += symbol
        col += 1

        if (col == numofcol) or (col == numofcol - 1 and row >= numofrow - numofshadedbox):
            
            col = 0
            row += 1

    return ''.join(plaintext)
if __name__ == '__main__':
    main()

