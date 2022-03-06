import time
import re
from datetime import datetime


def getUserNumberInput(inputMessage):
    numberInput = ''
    
    # Ensure the input is an integer
    while type(numberInput) != int:
        numberInput = input(inputMessage)
        if not numberInput.isdigit():
            print('Input must be a positive integer.\n')
        else:
            numberInput = int(numberInput)
    
    return numberInput
    





def getUserNumberInputWithEmptyDefault(inputMessage, emptyDefaultValue):
    numberInput = 'NOT_SET'
    
    # Ensure the input is an integer
    while type(numberInput) != int:
        numberInput = input(inputMessage)
        if len(numberInput) == 0:
            # Empty input means use the default value
            numberInput = emptyDefaultValue
        elif not numberInput.isdigit():
            print('Input must be a positive integer or leave empty for default value of ' + str(emptyDefaultValue) + '.\n')
        else:
            numberInput = int(numberInput)
    
    return numberInput
    




def getUserInputFromList(inputMessage, optionArray):
    userInput = ''

    optionsArrayString = '('

    for option in optionArray:
        optionsArrayString += option + ', '
    
    # Replace trailing ',' with ')'
    optionsArrayString = optionsArrayString[:-2] + ')'

    # Ensure the input is the option array
    while userInput not in optionArray:
        userInput = input(inputMessage + optionsArrayString + ' ')
        
        if userInput not in optionArray:
            print('Input must be on of the following: ' + optionsArrayString + '\n')
    
    return userInput




def getUserTimeInput(inputMessage):
    userInput = ''
    
    regexString = '^0[1-9]{1}|1[0-2]{1}:[0-5]{1}[0-9]{1} [AM|PM]{1}'
    regObj = re.compile(regexString)
    
    matches = regObj.findall(userInput)
    
    # Ensure the input is in HH:MM AM|PM format
    while len(matches) == 0:
        userInput = input(inputMessage + '(HH:MM AM|PM) ')
        
        matches = regObj.findall(userInput)
        
        if len(matches) == 0:
            print('Input must match regex: ' + regexString + '\n')
        else:
            print('Valid input: ' + str(userInput) + ' matches: ' + str(matches))
            userInput = datetime.strptime(userInput, '%I:%M %p').time()
            print('Confirmed time: ' + str(userInput))
    
    return userInput



