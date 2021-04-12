n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dp = [[min(a[n-1][0]+a[0][1],a[n-1][0]+a[0][2]),
      min(a[n-1][1]+a[0][0],a[n-1][1]+a[0][2]),
      min(a[n-1][2]+a[0][0],a[n-1][2]+a[0][1])],
      []*(n-2)]
for i in range(1,n-1) :
    dp[i].append(min(a[i][0]+dp[i-1][1],a[i][0]+dp[i-1][2]))
    dp[i].append(min(a[i][1]+dp[i-1][0],a[i][1]+dp[i-1][2]))
    dp[i].append(min(a[i][2]+dp[i-1][0],a[i][2]+dp[i-1][1]))
print(min(dp[n-2]))
    

            
