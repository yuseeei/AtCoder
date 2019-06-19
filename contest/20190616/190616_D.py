N, K = (map(int, input().split()))
a = list(map(int, input().split()))

s = 0
ans = 0

for j in range(K):   
    for i in range(N-j):
        if sum(a[s:s+j+1]) < K:
            now = sum(a[s:s+j+1])
#            print(s, i, j, now)
            s += 1
        elif sum(a[s:s+j+1]) >= K:
            now = sum(a[s:s+j+1])
            ans += 1
#            print(s, i, j, now, ans)
            s += 1
    s = 0
print(ans)   
