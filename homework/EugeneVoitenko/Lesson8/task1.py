import random


salary = int(input("Write your salary:"))
bonus = random.choice([True, False])
if bonus:
    print(f'{salary}, {bonus} - ${salary + random.randint(1, 1000)}')
else:
    print(f'{salary}, {bonus} - ${salary}')
