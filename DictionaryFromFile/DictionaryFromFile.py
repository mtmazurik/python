#!rgb_led
import ast                  # abstract syntax trees


def setup():
    file = open("colors.txt", "r")
    contents = file.read()
    global color_dict 
    color_dict = ast.literal_eval(contents)
    print(color_dict)

def destroy():
    file.close()

def main(): 
    while True:  
        userInput = input('What color? ')
        hexValueString = color_dict.get(userInput.upper(), "notfound" )
        if hexValueString != "notfound": 
            print(userInput.upper() + " is " + hexValueString)
        else:
            print('no color in file by that name')
                 
if __name__ == '__main__':          # todo: is this the entry point to the program? thesis: yes it is 
    setup()
    try:
        main()
    except KeyboardInterrupt:		# When 'Ctrl+C' is pressed, the program destroy() will be  executed.
        print('\nok. bye!\n')
        exit()