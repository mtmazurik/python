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
    tempCalcProgram = '/home/mtmazurik/python/CommandLineShell/Celsius_To_Fahrenheit_Calculator.py'
    print('type: e(xit) to leave')
    while True:  

        userInput = input('rsh> ')

        if userInput == '' : continue                    # handle no input  case
        cmd, convType, tempValue = parseInput(userInput) # separate the command line

        if cmd == ('e'):    # (e)xit
            break
        elif cmd == ('t'):  # (t)empcalc
            subprocess_cmd_args_list = ['python3', tempCalcProgram, convType, tempValue ]
            p = subprocess.call(subprocess_cmd_args_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            outputMessage = p.stdout.read()
            print(outputMessage)
        else:
            print('Command not recognized. Re-enter a valid command.')
                          
if __name__ == '__main__': 
    try:
        main()
    except AttributeError as exc:
        print(str(exc))
    except NameError as exc:
        print(str(exc))
    except KeyboardInterrupt:
        print('\nok. rsh says bye!\n')
        exit()
    except:
        print('Exception encountered.' + str(sys.exc_info()[0])) # this will tell what type of exception
        exit()