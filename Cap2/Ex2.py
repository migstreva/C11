num = int(input("Enter a number: "))
min_num = int(input("Enter minimum number: "))
max_num = int(input("Enter maximum number: "))

for i in range(int(min_num), int(max_num) + 1):
    result = num * i
    print(str(num) + " * " + str(i) + " = " + str(result))

