#!CommandLineShell
import subprocess
import sys
import logging

def main(): 
    while True:  
        userInput = input('rsh> ')
        userInput = userInput.upper()
        convertType = userInput[0]
        if convertType == ('E'):
            break
        elif convertType == ('T'):
            proc = subprocess.Popen("ls -l", shell=isinstance("ls -l", str),
                                stdin = PIPE,
                                stdout = PIPE,
                                stderr = STDOUT,
                                close_fds = True)
            print('\tsubprocess output: ' + str(stdout_value))
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