#!CommandLineShell
import subprocess

def main(): 
    while True:  
        userInput = input('rsh> ')
        userInput = userInput.upper()
        convertType = userInput[0]
        if convertType == ('E'):
            break
        elif convertType == ('T'):
            proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                                shell=True,
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE)
            stdout_value, stderr_value = proc.communicate('through stdin to stdout')
            print('\tpass through:', repr(stdout_value))
            print('\tstderr      :', repr(stderr_value))
        else:
            print('Command not recognized. Re-enter a valid command.')
                          
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
    except:
        print('Exception encountered. Restart program and try again.')
        exit()