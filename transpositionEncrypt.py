
import pyperclip 

def main():
    mymessage = 'my passwords are very simple'
    mykey = 4

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


