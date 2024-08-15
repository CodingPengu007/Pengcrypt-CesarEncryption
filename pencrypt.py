#ImportedObjects#
import random
import time

#starting program#
print("starting program...")
time.sleep(0.5)
print("started sucessfully")
time.sleep(0.1)

#version#
print("-> program version: 0.798 / stranded plaice")
print("   a encrypting software made by Pengu")
print("")

#other version-names#
#surfing penguins, Ice flowing, ice agent,

#used version-names#
#tangled penguin

#definitions#
def first_decision():

    decision_made = False
    while decision_made == False:
        print("Please press E to encrypt and U to unscramble messages.")
        answer = input("-> ")
        if answer in ["E", "e", "encrypt", "ecrypting mode"]:
            print("-> encrypting mode, activated")
            print("")
            decision_made = True
            encrypting_entrance()
        elif answer in ["U", "u", "unscrambling", "unscrambling mode"]:
            decision_made = True
            print("-> unscrambling mode, activated")
            print("")
            decision_made = True
            unscramble()
        else:
            print(" -> Sorry please press E or U thank you. ")
            print("")


def encrypt_or_unscramble():

    decision_made = False
    while decision_made == False:
        print("Please press E to encrypt and U to unscramble messages.")
        answer = input("-> ")
        if answer in ["E", "e", "encrypt", "ecrypting mode"]:
            print("-> encrypting mode, activated")
            print("")
            decision_made = True
            encrypting_entrance()
        elif answer in ["U", "u", "unscrambling", "unscrambling mode"]:
            print("-> unscrambling mode, activated")
            print("")
            decision_made = True
            unscramble()
        else:
            print(" -> Sorry please press E or U thank you. ")
            print("")


def encrypting_entrance():

    print("Lets encrypt your text message!")
    print("-------------------------------------------->")
    print("Firstly we need an Pencrypting-Code, you can choose your")
    print("own code between 1 and 26 or can use a random Code.")
    encrypt()


def encrypt():

    code = 1
    owncode = 1
    decision_made = False
    print("-> Please press O to use your own Code and R to get an random Code,")
    print("   you also can exit encrypting mode with X.")

    while decision_made == False:
        answer = input("-> ")
        print("")
        if answer in ["O", "o", "own", "own code", "Own", "Own Code", "0"]:
            print("")
            print("-> Please enter your own code from 1 to 26 or exit with X")
            while True:
                owncode = input("-> ")
                if owncode in ["X", "x", "Exit", "exit"]:
                    print("-> Exiting self-choosing mode")
                    decision_made = True
                    encrypt()
                    break
                elif owncode.isdigit():
                    if 1 <= int(owncode) <= 25:
                        code = int(owncode)
                        decision_made = True
                        break
                    else:
                        print("-> Sorry, please enter a number between 1 and 26 or X to exit.")
                        print("")
                else:
                    print(" -> Sorry, please enter a number or X to exit.")
                    print("")
        elif answer in ["R", "r", "random", "random code"]:
            code = random.randint(1,25)
            decision_made = True
        elif answer in ["X", "x", "Exit", "exit"]:
            print("-> Exiting encrypting mode")
            print("")
            decision_made = True
            encrypt_or_unscramble()
        else:
            print(" -> Sorry please press O, R or X thank you. ")
            print("")
    print(f"Nice, your Pencrypting-Code is {code}, now we can start encrypting your textmessage.")
    message = input("Please enter it here: ")
    #encrypting#
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + code) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    print(f"Your encrypted message: {encrypted_message}")
    print(f"The message got created with the Pencrypt-Code {code}")


def unscramble():

    print("-> Lets unscramble your text message!")
    print("")

    decision_made = False
    while decision_made == False:
        print("-> Please enter your Pencrypt-Code from 1 to 26")
        print("   or exit unscrambling mode with X.")
        answer = input("-> ")
        if answer in ["X", "x", "Exit", "exit"]:
            print("-> Exiting unscrambling mode")
            print("")
            decision_made = True
            encrypt_or_unscramble()
        elif answer.isdigit():
            if 1 <= int(answer) <= 25:
                code = int(answer)
                decision_made = True
            else:
                print(" -> Sorry, please enter a number between 1 and 26 or X to exit.")
                print("")
        else:
            print(" -> Sorry, please enter your Pencrypt-Code or press X to exit.")
            print("")

    print("Nice, now we can start unscrambling your textmessage.")
    message = input("Please enter it here: ")
    #unscrambling#
    unscrambled_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            unscrambled_char = chr((ord(char) - ascii_offset - code) % 26 + ascii_offset)
            unscrambled_message += unscrambled_char
        else:
            unscrambled_message += char
    print(f"Your unscrambled message: {unscrambled_message}")
    print(f"The message got unscrambled with the Pencrypt-Code {code}")


#welcome dialog#
print("Welcome to Pencrypt, your nice and easy software to encrypt and")
print("unscramble textmessages with the caesar encryption technique.")
print("")

#Pencrypt Code#
print("Now you can encrypt a message for others or unscramble messages from others,")
print("")
first_decision()
input("Press Enter to exit...")