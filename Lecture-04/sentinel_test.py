keep_going = 'y'

while keep_going == 'y':
    wholesale = float(input("Enter the item's wholesale: "))

    retail_price = wholesale * 2.5
    print(f'The retail_price is: ${retail_price:.2f}')

    keep_going = input('Do you have another item? (Enter y for yes): ')