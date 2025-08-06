distance = int(input("Enter distance in kilometers: "))

if distance <= 200:
    price = distance * 0.50
elif distance > 200:
    price = distance * 0.45

print("The price is $", price)