# setip.py - network setting on ubuntu command
import sys
import subprocess

# disks       
# usage  rsh> disks
#                      invokes df -h command
def main(): 
    if len(sys.argv) != 1:                          
        print('invalid command.   Example usage:   rsh> disks')
        exit()

    # linux 
    df_args = ['df', '-h' ]
    raw2 = subprocess.check_output(df_args)
    output = raw2.decode('utf-8')
    print(output)
                          
if __name__ == '__main__': 
    try:
        main()
    except:
        print('disks. Check command and retry.')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"Type: {exc_type}\nValue: {exc_value}\nTB: {exc_tb}")
        exit()