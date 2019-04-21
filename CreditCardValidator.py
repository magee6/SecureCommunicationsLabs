def str2Int(number):
    return [int(x) for x in str(number)]

def validity_check(card_num):
    if len(card_num) >= 13 and len(card_num) <= 19:
        nums = str2Int(card_num)
        odd_nums = nums[-1::-2]
        even_nums = nums[-2::-2]
        result = sum(odd_nums)
        for num in even_nums:
            result += sum(str2Int(2 * num))
        return result % 10 == 0

def checksum(card_num):
        nums = str2Int(card_num)
        odd_nums = nums[-1::-2]
        even_nums = nums[-2::-2]
        result = sum(odd_nums)
        for num in even_nums:
            result += sum(str2Int(2 * num))
        print(result)
        check_calc = str2Int(result * 9 % 10)
        print("The check digit for your card is >>> ", str(check_calc))

def vendor_check(card_num):
    numbers = str2Int(card_num)
    if validity_check(card_num):
        if card_num[0:2] == '51' or card_num[0:2] == "52" or card_num[0:2] == "53" or card_num[0:2] == "54" or card_num[0:2] == "55":
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
        elif card_num[0:2] == "54":
            print("Card Vendor >>> Diners Club - USA & Canada")
        elif card_num[0:2] == "54":
            print("Card Vendor >>> Diners Club - USA & Canada")
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
retry = True
while retry:
    print("#############################################")
    print("<<<<<<<<<< Credit Card Validator >>>>>>>>>>")
    print("A) Verify Card")
    print("B) Vendor Check")
    print("C) Checksum calculation")
    print("D) Select Vendor + generate random valid card")
    print("E) Exit \n")
    print("#############################################")

    choice = str(input("Please choose an option A,B,C,D or E >>> "))

    if choice == "A" or choice == "a":
        print("You chose >>> Verify Card")
        card_num = input("Enter credit card number >>> ")
        if validity_check(card_num):
            print("Checking...This is a valid card")
        else:
            print("Checking...This is an invalid card")

    elif choice == "B" or choice == "b":
        print("You chose >>> Vendor Check")
        card_num = str(input("Enter credit card number >>> "))
        vendor_check(card_num)

    elif choice == "C" or choice == "c":
        print("You chose >>> Checksum calculation")
        card_num = str(input("Enter the first portion of your card >>> "))
        checksum(card_num)

    elif choice == "D" or choice == "d":
        print("D")
    elif choice == "E" or choice == "e":
        print("Exiting...")
        retry = False
    else:
        print("Invalid option, choose again")
