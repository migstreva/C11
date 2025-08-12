people_list = []
age_list = []
gender_list = []

n = int(input("Type number of people: "))
for i in range(n):
    people_list.append(input("Type person's name: "))
    age_list.append(float(input("Type person's age: ")))
    gender_list.append(input("Type person's sex: "))

sum = 0
for i in range(n):
    sum += age_list[i]
print(sum/n)

under_20_females = 0
for i in range(n):
    if age_list[i] < 20 and gender_list[i] == 'female':
        under_20_females += 1
print(under_20_females)