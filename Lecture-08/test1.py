with open("employees.txt", "r") as file:
    line = file.readlines()

while line != '':
       emp_id = file.readline().strip()
       dept = file.readline().strip()

print('Name:', name.strip())
print('ID:', emp_id)
print('Department:', dept) 

name = file.readlines()