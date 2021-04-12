N,M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(M)]
a.sort()
dp = [1]*N
for i in range(M) :
    if dp[a[i][1]-1] < dp[a[i][0]-1] + 1 :
        dp[a[i][1]-1] = dp[a[i][0]-1] + 1
print(dp)

        
