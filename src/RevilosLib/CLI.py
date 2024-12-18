import keyboard
import time

def cls():
    print("\033[H\033[J", end="")

def userInputMenu(menyItems, menyName="", wrapAround = False, returnInt = False, clearOnExit = True):

    if type(menyItems) != list:
        raise TypeError("MenyOptions must be a list")
    if type(menyName) != str:
        raise TypeError("MenyName must be a string")
    if type(wrapAround) != bool:
        raise TypeError("wrapAround must be a bool")
    if type(returnInt) != bool:
        raise TypeError("returnInt must be a bool")
    if type(clearOnExit) != bool:
        raise TypeError("clearOnExit must be a bool")

    currentlySelected = 0
    update = True
    menyOptionsLen = len(menyItems)

    while True:

        if keyboard.is_pressed('down') and not update:
            update = True
            if currentlySelected < menyOptionsLen - 1:
                currentlySelected += 1
            elif wrapAround == True:
                currentlySelected = 0

        if keyboard.is_pressed('up') and not update:
            update = True
            if currentlySelected > 0:
                currentlySelected -= 1
            elif wrapAround == True:
                currentlySelected = menyOptionsLen - 1

        if keyboard.is_pressed('enter') and not update:
            if clearOnExit:
                cls()
            if returnInt:
                return currentlySelected
            else:
                return menyItems[currentlySelected]

        if update:
            update = False
            cls()
            if menyName != "":
                print(menyName)
            for i in range(menyOptionsLen):
                if i == currentlySelected:
                    print("->", menyItems[i])
                else:
                    print("  ", menyItems[i])
            time.sleep(0.1)

def userInput(questionMessage, inputType, minVal=None):

    if type(questionMessage) != str:
        raise TypeError("questionMessage must be a string")
    if not inputType in ["str","int","bool"]:
        raise SyntaxError("inputType is not a valid type")
    if type(minVal) != int:
        raise TypeError("minVal must be a integer")

    while True:
        userInput = input(questionMessage)

        if inputType == "str":
            return userInput
        
        elif inputType == "bool":
            if userInput.lower() in ("true", "y", "yes"):
                return True
            elif userInput.lower() in ("false", "n", "no"):
                return False
            else:
                cls()
                print("Please enter a valid answer (true/false, y/n, yes/no)")
        
        elif inputType == "int":
            try:
                userInputInt = int(userInput)
                if minVal is not None and userInputInt < minVal:
                    print(f"Please enter an integer greater than or equal to {minVal}")
                else:
                    return userInputInt
            except ValueError:
                print("Please enter a valid integer")
        
        else:
            print("Invalid type")
        return None
