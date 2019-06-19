N, X = map(int, input().split())
LIST = list(map(int,input().split()))

RES = []
ichi = 0
RES.append(ichi)
for i in LIST:
    ichi = ichi + i
    RES.append(ichi)

cnt = 0
for i in RES:
    if i <= X:
        cnt = cnt + 1

print(cnt)
