import random

def randomString(Length, Uppercase = True, Lowercase = True, Numbers = True, Symbols = True):

    if type(Length) != int:
        raise TypeError("Length must be a integer")
    # TODO: Add better Error handeling


    lettersCharacter = "abcdefghijklmnopqrstuvwxyz"
    bigLettersCharacter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbersCharacter = "1234567890"
    symbolsCharacter = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    characterList = ""

    if Uppercase:
        characterList += bigLettersCharacter
    if Lowercase:
        characterList += lettersCharacter
    if Numbers:
        characterList += numbersCharacter
    if Symbols:
        characterList += symbolsCharacter
    
    return ''.join(random.choice(characterList) for _ in range(Length))

def fastRandomString(Length):
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?") for _ in range(Length))

# TODO: Add more random ID generator functions. Example: Card, Phone, Address.
