import sys

rot = sys.argv[1]
ciphertext = sys.argv[2]

def rot5(x):
    output1 = " "

    for i in x:
        dec = ord(i)

        if dec >= ord('0') and dec <= ord('9'):
            if dec <= ord('4'):
                dec += 5
            else:
                dec -= 5

        output1 += chr(dec)

    print(output1)

def rot13(y):
    output2 = " "

    for i in y:
        alpha = ord(i)                                             #alpha is assigned to the returned integer of the Unicode character

        if alpha >= ord('a') and alpha <= ord('z'):               #if alpha is greater than or equal to ascii a AND less than or equal to ascii z

            if alpha > ord('m'):                                   #if character is  greater than ascii m, go back 13 characters
                alpha -= 13
            else:
                alpha += 13                                        #otherwise go forward 13 characters

        elif alpha >= ord('A') and alpha <= ord('Z'):             #if alpha is greater than or equal to ascii A AND less than or equal to ascii Z

            if alpha > ord('M'):                                   #if character is  greater than ascii M, go back 13 characters
                alpha -= 13
            else:
                alpha += 13                                        #otherwise go forward 13 characters

        output2 += chr(alpha)                                      #returns the string and is assigned to the output2 variable
    print(output2)

def rot47(z):
    output3 = " "

    for i in z:

        all = ord(i)

        if all >= ord('!') and all <= ord('~'):

            output3 += (chr(33 + ((all + 14) % 94)))

        else:
            output3 += ord(i)

    output3 += chr(all)

    print(output3)


if rot == 'dec':
    rot5(ciphertext)
elif rot == "alpha":
    rot13(ciphertext)
elif rot == "all":
    rot47(ciphertext)
else:
    print("Please enter arguments 'dec'(rot5), 'alpha'(rot 13) or 'all'(rot 47) + ciphertext")




