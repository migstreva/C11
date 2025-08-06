while True:
    num = int(input("Enter a number from 1000 to 9999: "))
    if num < 1000 or num > 9999:
        continue
    else:
        break

num_str = str(num)
unit = num_str[-1]
ten = num_str[-2]
hundred = num_str[-3]
thousand = num_str[-4]
print("Unit:", unit)
print("Ten:", ten)
print("Hundred:", hundred)
print("Thousand:", thousand)