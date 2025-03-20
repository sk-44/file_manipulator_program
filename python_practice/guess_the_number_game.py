import random

min_val = int(input("minimum value: "))
max_val = int(input("maximum value: "))

if min_val > max_val:
    print("minimum value is smaller than maximum value.")

rand_val = random.randint(min_val, max_val)

for i in range(5):
    print(f"あと{5 - 1}回")
    ans = int(input("random value is: "))
    if rand_val == ans:
        print("Success!")
        break
    else:
        if i < 4:
            print("No... one more!")
        else:
            print("Game over")

