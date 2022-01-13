import math, pyperclip

def main():
    mymessage = 'mao  ymysrav p sdreslpwserie'
    mykey = 4

    plaintext = encryptMessage(mykey, mymessage)

    print(plaintext + '|')

    pyperclip.copy(plaintext)

def encryptMessage(key, message):
    numofcol = math.ceil(len(message) / key)

    numofrow = key

    numofshadedbox = (numofcol * numofrow) - len(message)

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

