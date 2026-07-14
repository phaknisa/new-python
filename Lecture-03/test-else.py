# if conditition1:
    # code to execute if condition1 is True
# elif condition2:
    # code to execute if condition2 is True

# Input the number of employees from the user
num_employees = int(input("Enter the number of employees: "))
# Check the number of employees and print the appropriate company size
if num_employees < 50:
    print("This is a small company.")
elif num_employees < 250:
    print("This is a medium-sized company.")
else:
    print("This is a large company.")
