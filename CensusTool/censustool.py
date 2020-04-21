#cencustool.py
import csv      # see; https://docs.python.org/3/library/csv.html
import locale

def main():
    with open('US-Census-Metro-Data.csv') as csvfile:
       rdr = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
       next(rdr, None) # skip first (header row) in .CSV file
       i = 0
       for row in rdr:
           i = i + 1
           metro = str(row[4])          # 5th column of data is NAME
           population2019 = str(row[17])    # 18th column of data is POPESTIMATE2019
           metroArray = metro.split(',')
           pop2019 = int(population2019)
           print(f'{metro}\t{pop2019:,}')  # todo: pretty up output, read here: https://scientificallysound.org/2016/10/17/python-print3/
           
    print(f'\nCount: {i}')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:		# When 'Ctrl+C' is pressed, the program destroy() will be  executed.
        print('\nok. bye!\n')
        exit()