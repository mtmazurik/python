#!CommandLineShell
import subprocess
import sys
import logging

def main(): 
    print('type: e(xit) to leave')
    while True:  
        userInput = input('rsh> ')
        userInput = userInput.lower()
        commandType = userInput[0]
        if commandType == ('e'):
            break
        elif commandType == ('t'):
            out, err = subprocess.Popen(userInput, shell=True,
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.STDOUT,
                                close_fds = True).communicate()
            print('\tsubprocess output: ' + str(out))
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