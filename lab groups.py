students = int(input("Enter the number of students:\n "))
fullGroups = students // 24
remaining = students % 24

print(fullGroups, " full groups.", remaining, " remaining")
