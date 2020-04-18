#!Celsius_To_Fahrenheit_Calculator 
import sys
from Temperature import CtoF, FtoC, KtoF

def getNumericTemperature(promptString):
    while True:
        try:
            inputVal = input('(' + promptString + ')value? ')
            return float(inputVal)
        except KeyboardInterrupt:
            raise
        except:
            print("Input must be a float")
            
def main(): 
    if len(sys.argv) > 1 :          # we are being called by command line with arguments (note: will be lowercase convertType)
        print(sys.argv) # debug
        convType = argv[1]
        tempVal = float(argv[2])
        if convType == ('c')
            print(str(round(CtoF(tempVal)) + ' F')
        elif convType == ('f')
            print(str(round(FtoC(tempVal)) + ' C')
        elif confType == ('k')
            print(str(round(KtoF(tempVal))) + 'F')
        else
            print('invalid input; example usage:  tempcalc f 212')
    else:
# interactive loop
    while True:  
        userInput = input('Convert (C)elsius, (F)ahrenheit, or (K)elvin? ')
        userInput = userInput.upper()
        convertType = userInput[0]
        if convertType == ('C'):
            celsius = getNumericTemperature('celsius')
            fahrenheitOutput = CtoF(celsius)
            print(str(round(fahrenheitOutput, 1)) + ' F')
        elif convertType == ('F'):
            fahrenheit = getNumericTemperature('fahrenheit')
            celsiusOutput = FtoC(fahrenheit)
            print(str(round(celsiusOutput, 1)) + ' C')   
        elif convertType == ('K'):
            kelvin = getNumericTemperature('kelvin')
            kelvinOutput = KtoF(kelvin)
            print(str(round(kelvinOutput, 1)) + 'F')         
        else:
            print('Please choose either (C)elsius or (F)ahrenheit')
                          
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
    except:
        print('Exception encountered. Restart program and try again.')
        exit()