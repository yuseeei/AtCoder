INPUT = list(map(int, input().split()))

x = INPUT[2]
y = INPUT[3]

cx = INPUT[0]/2
cy = INPUT[1]/2

min_area = INPUT[0]*INPUT[1]/2

if x == cx and y == cy:
    print(min_area,1)
else:
    print(min_area,0)
