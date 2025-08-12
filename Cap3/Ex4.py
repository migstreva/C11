name = ''
weight = 0
weights_table = {name:weight}

for i in range(3):
    name = input("Type person's name: ")
    weights_table[name] = float(input("Type person's weight: "))

del weights_table['']
print(min(weights_table.values()))

