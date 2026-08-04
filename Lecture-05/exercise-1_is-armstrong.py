def is_armstrong(num):
    # Convert the number to a string to get the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of the digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num

print(is_armstrong(153))  # Output: True (153 = 1^3 + 5^3 + 3^3)
print(is_armstrong(9474))  # Output: True (9474 = 9^4 + 4^4 + 7^4 + 4^4)
print(is_armstrong(123))  # Output: False (123 is not an Armstrong number)