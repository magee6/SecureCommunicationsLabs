import sys

rot = sys.argv[1]                                               # takes in second commandline argument as dec, alpha or all
ciphertext = sys.argv[2]                                        # takes in the text to be encoded into the third argument

def rot5(x):                                                    # function takes in a text to be encoded in variable x as an argument.
    output1 = " "

    for i in x:                                                 # iterates through each digit which was passed into the function
        dec = ord(i)                                            # dec is assigned to the integer representing the ascii character

        if dec >= ord('0') and dec <= ord('9'):                 # if the dec integer is greater than or equal to the 47 and less than 57
            if dec <= ord('4'):                                 # if dec is less than or equal to 52, shift 5 characters forward
                dec += 5
            else:                                               # else shift 5 characters backwards
                dec -= 5

        output1 += chr(dec)                                     # each shifted character is concatenated togther and stored in a variable output1

    print(output1)
                                                                # https://www.dotnetperls.com/rot13-python some code taken from here for this function
def rot13(y):                                                   # Takes in text in the variable y
    output2 = " "

    for i in y:                                                 # Iterates through each character in the string which is passed into the function
        alpha = ord(i)                                          # alpha is assigned to the returned integer of the Unicode character

        if alpha >= ord('a') and alpha <= ord('z'):             # if alpha character is greater than or equal to ascii decimal value 97 AND less than or equal to ascii decimal 122

            if alpha > ord('m'):                                # if character is  greater than ascii decinal 109, shift backward 13 characters
                alpha -= 13
            else:
                alpha += 13                                     # otherwise go forward 13 characters

        elif alpha >= ord('A') and alpha <= ord('Z'):           # if alpha is greater than or equal to ascii decimal 65 AND less than or equal to ascii decimal 90

            if alpha > ord('M'):                                # if character in alpha is greater than ascii decimal value 77, go back 13 characters
                alpha -= 13
            else:
                alpha += 13                                     # otherwise go forward 13 characters

        output2 += chr(alpha)                                   # returns and conncatanates the characters which represent the integer values in the ascii table to output2
    print(output2)

def rot47(z):
    output3 = " "

    for i in z:

        all = ord(i)

        if all >= ord('!') and all <= ord('~'):

            output3 += (chr(33 + ((all + 14) % 94)))            # subtracts 14 from cipher, mod 94, remainder added to 33 , character is the converted to character value.

        else:
            output3 += ord(i)

    output3 += chr(all)

    print(output3)

def bruteforce(k, cipher):

    output4 = " "                                               # empty string which will hold the decoded cipher

    for i in cipher:                                            # Iterates through the characters of the ciphertext and takes away the shift value
        val = (ord(i) - k) % 126

        if val < 32:                                            # if the integer value representing the character is less than 32, 95 is added.
            val += 95
        output4 += chr(val)                                     # integer values are converted to their respective characters and outputted to the variable output4

    print(output4)

if rot == 'dec':
    rot5(ciphertext)
elif rot == "alpha":
    rot13(ciphertext)
elif rot == "all":
    rot47(ciphertext)
elif rot == "brute":
    for i in range(1, 95, 1):                                   #iterates from 1 to 95 in a step of 1. This is the shift key value
        bruteforce(i, ciphertext)
else:
    print("Please enter arguments 'dec'(rot5), 'alpha'(rot 13) or 'all'(rot 47) + ciphertext")




