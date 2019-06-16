nx = list(map(int, input().split()))
l = list(map(int, input().split()))
x = nx[1]
n = nx[0]
d = 0

for i in range(101):
    d = d + l[i]
    print(d)
    if d >= x:
        print(i+1)
        break
