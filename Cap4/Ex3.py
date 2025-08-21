import numpy as np

arr = np.zeros([2, 2])
i, j = np.random.randint(0, 2, 2)
arr[i, j] = 1
print(arr)
failed = False
x = -1
y = -1

for i in range(3):
    while not(0 <= x <= 1 and 0 <= y <= 1):
        x, y = int(input("Enter position x: ")), int(input("Enter position y: "))
    if arr[x, y] == 1:
        print("Game Over! Try again!")
        failed = True
        break
if not failed:
    print("Congratulations! You beat the game!")
