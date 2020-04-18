#!CommandLineShell
import subprocess
import sys
import logging

def parseInput(inputString):
    inputString = inputString.lower()       #lower case it all
    inputArray = inputString.split()        # break line by white space into inputs[] array

    cmdstring = inputArray[0]               # grab the first chars:   (t)empcalc command
    cmd = cmdstring[0]                      # pluck of the first char

    conversionType = None
    temperatureValue = None
    if len(inputArray) > 1 :
        conversionType = inputArray[1]         # grab the 2nd chars
    if len(inputArray) > 2 :
        temperatureValue = inputArray[2]       # grab the 3rd chars 

    return cmd, conversionType, temperatureValue  # return 3 values from a function

def main(): 
    pythonCommand = 'python3 /home/mtmazurik/python/CommandLineShell/Celsius_To_Fahrenheit_Calculator.py'
    print('type: e(xit) to leave')
    while True:  

        userInput = input('rsh> ')

        if userInput == '' : continue                    # handle no input  case
        cmd, convType, tempValue = parseInput(userInput) # separate the command line

        if cmd == ('e'):    # (e)xit
            break
        elif cmd == ('t'):  # (t)empcalc
            cmd_list = [pythonCommand, convType, tempValue ]

            p = subprocess.call(cmd_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout = p.stdout.read()
            
            print(stdout)
        else:
            print('Command not recognized. Re-enter a valid command.')
                          
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
    except NameError as exc:
        print(str(exc))
    except:
        print('Exception encountered.' + str(sys.exc_info()[0])) # this will tell what type of exception
        exit()