import time






def getNumberInput(inputMessage):
    numberInput = ''
    
    # Ensure the input is an integer
    while type(numberInput) != int:
        numberInput = input(inputMessage)
        if not numberInput.isdigit():
            print('Input must be a positive integer.\n')
        else:
            numberInput = int(numberInput)
    
    return numberInput
    
    

def configureTest():
    
    testDuration = getNumberInput('Test Duration (seconds): ')
    
    print(str(testDuration))







try:
    configureTest()
finally:
    print('End')
