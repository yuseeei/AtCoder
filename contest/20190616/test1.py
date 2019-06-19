import random

while True:
    a = random.randint(1, 13)
    b = random.randint(1, 13)
    c = random.randint(1, 13)
    print(a)
    if (a+b+c) > 21:
        print('end')
        break
