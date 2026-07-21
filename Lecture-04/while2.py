keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comma_rate = float(input('Enter the commission rate: '))

    commission = sales * comma_rate
    print(f'The commission is: ${commission:.2f}')

    keep_going = input('Do you want to claculate another' + \
                       'commission (Enter y for yes): ')