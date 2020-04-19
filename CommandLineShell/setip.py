# setip - network setting on ubuntu command
# note: assuming 'eth0' is the network device for Virtual Machine ubuntu installations
#
# usage  rsh> setip 10.1.1.50 255.255.255.0 10.1.1.1       ( ip_address   subnet_mask   gateway)
import subprocess

def main(): 
    if len(sys.argv) == 4:                           # we are being called by command line with arguments (note: will be lowercase convertType)
        ip_address = sys.argv[1]
        mask = sys.argv[2]
        gateway = sys.argv[3]
    else:
        print('invalid input; example usage:  setip 10.1.1.50 255.255.255.0 10.1.1.1     ( ip_address subnet_mask  gateway)')

    netInterface = 'eth0'        
    ipargs = ['sudo', 'ifconfig', netInterface, ip_address, "netmask", mask ]
    raw1 = subprocess.check_output(ipargs)       # returns byte type
    outputMessage1 = raw1.decode('utf-8').rstrip()) 
    routeargs = ['sudo', 'route', 'add', 'default', "gw", gateway, netInterface ]
    raw2 = subprocess.check_output()
    outputMessage2 = raw2.decode('utf-8').rstrip()) 
    outputMessage = outputMessage1 + '/n' + outputMessage2
    print(outputMessage)
                          
if __name__ == '__main__': 
    try:
        main()
    except:
        print('setip error encountered. Check command and retry.')
        exit()