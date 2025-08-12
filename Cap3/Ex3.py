name = input("Type student's name: ")
grade = float(input("Type student's grade: "))
grade_table = {name:grade}

if grade_table[name] >= 50:
    print("'AP'")
else:
    print("'RP'")
