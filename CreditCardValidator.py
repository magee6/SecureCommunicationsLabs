import random

def str2Int(number):                                                                        # takes in a string, Converts string into an array of numbers
    return [int(x) for x in str(number)]
                                                                                            # parts of validity_check taken from https://stackoverflow.com/questions/39272087/validate-credit-card-number-using-luhn-algorithm-python
def validity_check(card_num):                                                               # takes in a string in the variable card_num
    if len(card_num) >= 13 and len(card_num) <= 19:                                         # checks if length of number is greater than 13 and less than 19
        nums = str2Int(card_num)
        odd_nums = nums[-1::-2]                                                             # stores odd numbers in the array, starts on last digit and stores every 2nd digit in reverse in an array odd_nums
        even_nums = nums[-2::-2]                                                            # stores even numbers in the array, starts on second last digit and stores every 2nd digit in reverse in an array even_nums
        result = sum(odd_nums)                                                              # sum of the array odd_nums stored in result
        for num in even_nums:
            result += sum(str2Int(2 * num))                                                 #iterates through the array even_nums doubling each element and adding it to the sum of odd_nums.
        return result % 10 == 0                                                             #if the result has no remainder it returns true

def checksum(card_num):
        nums = str2Int(card_num)
        odd_nums = nums[-1::-2]
        even_nums = nums[-2::-2]
        result = sum(odd_nums)
        for num in even_nums:
            result += sum(str2Int(2 * num))
        print("Result without check digit " ,result)
        check_calc = str2Int(result * 9 % 10)                                               # the result multiplied by 9 mod 10 to give the check digit value
        print("The check digit for your card is >>> ",str(check_calc))
        return check_calc

def vendor_check(card_num):
    numbers = str2Int(card_num)
    if validity_check(card_num):
        if card_num[0:2] == '51' or card_num[0:2] == "52" or card_num[0:2] == "53" or card_num[0:2] == "54" or card_num[0:2] == "55":                                           # checks if first two elements in the integer are 51, 52, 53...
            print("Card Type >>> Mastercard")
        elif card_num[0:4] == "4026" or card_num[0:4] == "4508" or card_num[0:4] == "4844" or card_num[0:4] == "4913" or card_num[0:4] == "4917" or card_num[0:6] == "417500":
            print("Card Vendor >>> Visa Electron")
        elif card_num[0:1] == "4":
            print("Card Vendor >>> Visa")
        elif card_num[0:2] == "37":
            print("Card Vendor >>> American Express")
        elif card_num[0:3] == "300" or card_num[0:3] == "301" or card_num[0:3] == "302" or card_num[0:3] == "303" or card_num[0:3] == "304" or card_num[0:3] == "305":
            print("Card Vendor >>> Diners Club - Carte Blanche")
        elif card_num[0:2] == "36":
            print("Card Vendor >>> Diners Club - International")
        elif card_num[0:2] == "54" or card_num[0:2] == "55":
            print("Card Vendor >>> Diners Club - North America")
        elif card_num[0:4] == "6011":
            print("Card Vendor >>> Discover")
        elif card_num[0:3] == "637" or card_num[0:3] == "638" or card_num[0:3] == "639":
            print("Card Vendor >>> InstaPayment")
        elif numbers[0:4] in range (3528,3589):
            print("Card Vendor >>> JCB")
        elif card_num[0:4] == "5018" or card_num[0:4] == "5020" or card_num[0:4] == "5038" or card_num[0:4] == "5893" or card_num[0:4] == "6304" or card_num[0:4] == "6759" or card_num[0:4] == "6761" or card_num[0:4] == "6762" or card_num[0:4] == "6763":
            print("Card Vendor >>> Maestro")
        else:
            print("Card Vendor >>> Unknown")

def generate_credit_card(card_vendor):

    while True:
        numbers = [random.randint(0, 9) for i in range(0, 16)]                              # generate random numbers in the range from 0 to 9.

        if card_vendor == "A" or card_vendor == "a":                                        # if user chose A, the first two number of their generated card will be 5 and 2.
            numbers[:2] = [5,2]
        if card_vendor == "B" or card_vendor == "b":
            numbers[0] = 4
        if card_vendor == "C" or card_vendor == "c":
            numbers[:4] = [4,0,2,6]
        if card_vendor == "D" or card_vendor == "d":
            numbers[:3] = [3,0,0]
        if card_vendor == "E" or card_vendor == "e":
            numbers[:2] = [3,6]
        if card_vendor == "F" or card_vendor == "f":
            numbers[:2] = [5,4]
        if card_vendor == "G" or card_vendor == "g":
            numbers[:4] = [6,0,1,1]
        if card_vendor == "H" or card_vendor == "h":
            numbers[:3] = [6,3,7]
        if card_vendor == "I" or card_vendor == "i":
            numbers[:4] = [5,0,1,8]

retry = True
while retry:                                                                           # while loop to continuosly show the menu until the user chooses to exit the program
    print("#############################################")
    print("<<<<<<<<<< Credit Card Validator >>>>>>>>>>")
    print("A) Verify Card")
    print("B) Vendor Check")
    print("C) Checksum calculation")
    print("D) Select Vendor + generate random valid card")
    print("E) Exit \n")
    print("#############################################")

    choice = str(input("Please choose an option A,B,C,D or E >>> "))                  # asks user to input a choice A,B,C,D or E

    if choice == "A" or choice == "a":                                                # if user chooses A they will be asked to enter a credit card number to be validated
        print("You chose >>> Verify Card")
        card_num = input("Enter credit card number >>> ")
        if validity_check(card_num):                                                  # number which has been entered will be passed to the validity_check function to be verified
            print("Checking...This is a valid card")
        else:
            print("Checking...This is an invalid card")

    elif choice == "B" or choice == "b":                                             # if user chooses B they will be prompted to enter their card number, the card will be passed to a function called vendor_check
        print("You chose >>> Vendor Check")
        card_num = str(input("Enter credit card number >>> "))
        vendor_check(card_num)

    elif choice == "C" or choice == "c":                                             # if user chooses C they will be prompted to enter the numbers of their card excluding the last digit to calculate the check digit
        print("You chose >>> Checksum calculation")
        card_num = str(input("Enter the first portion of your card >>> "))
        checksum(card_num)

    elif choice == "D" or choice == "d":
        print("You chose >>> Vendor Check")
        print("#############################################")
        print("<<<<<< Choose Vendor to Generate Card >>>>>>")
        print("A) Mastercard")
        print("B) Visa")
        print("C) Visa Electron")
        print("D) American Express")
        print("E) Diners Club - Carte Blanche")

        print("F) Diners Club - International")
        print("G) Diners Club - North America")
        print("H) Discover")
        print("I) Maestro")
        print("#############################################")
        card_vendor = str(input("Choose Vendor to generate >>> "))
        print("Generating...")
        print(generate_credit_card(card_vendor))


    elif choice == "E" or choice == "e":
        print("Exiting...")
        retry = False
    else:
        print("Invalid option, choose again")
