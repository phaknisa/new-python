# Attendance record for a week (each list represents a day's attendance)
attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],   #Day 1
    ["Alice", "Charline", "David"],         #Day 2
    ["Alice", "Bob", "David"],              #Day 3
    ["Alice", "David", "Eve"],              #Day 4
    ["Bob", "Charlie", "David"]             #Day 5
]

# 1. Find the set of students who were present every day.
# 2. Determine the set of students who were absent at least one day.
# 3. Create a list of students who were present on the first day but absent on the last day.
# 4. Calulate the total number of unique students who attended at least one day.

# Convert each day's attendance list into a set
attendance_set = [set(day) for day in attendance_week]
print(attendance_set)

# 1. Find the set of students who were present every day.
present_every_day = set.intersection(*attendance_set)
print("Present every day:", present_every_day)
# Output: {'David'}

# 2. Determine the set of students who were absent at least one day.
all_students = set.union(*attendance_set)
absent_at_least_one_day = all_students - present_every_day
print("Absent at least one day:", absent_at_least_one_day)
# Output: {'Alice', 'Charlie', 'Bob','Eve'}

# 3. Create a list of students who were present on the first day but absent on the last day.
first_day_present = attendance_set[0]
last_day_present = attendance_set[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day:", first_day_but_not_last)
#Output: ['Alice']

# 4. Calculate the total number of unique students who attended at least one day.
unique_students_count = len(all_students)
print("Total unique students:", unique_students_count)
# Output: 5

attendance_set = [
    {"Alice", "Bob", "Charlie"},
    {"Alice", "David", "Charlie"},
    {"Bob", "David", "Eva"}
]