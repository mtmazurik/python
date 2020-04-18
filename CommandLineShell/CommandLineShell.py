#!CommandLineShell
import subprocess
import sys
import logging

def main(): 
    print('type: e(xit) to leave')
    while True:  
        userInput = input('rsh> ')
        if userInput == '' : continue
        userInput = userInput.lower()
        commandType = userInput[0]
        if commandType == ('e'):
            break
        elif commandType == ('t'):
            cmd_list = ['./Celcius_to_Fahrenheit_Calculator.py', sys.argv[1], sys.argv[2] ]
            p = subprocess.Popen(cmd_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout = p.stdout.read()
            stderr = p.stderr.read()
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