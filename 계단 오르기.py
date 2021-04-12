n = int(input())
a = [int(input()) for _ in range(n)]
dp = [a[0],a[0]+a[1],max(a[0]+a[1],a[0]+a[2],a[1]+a[2])]
for i in range(3,n-1) :
    dp.append(max(dp[i-3]+a[i-1]+a[i],dp[i-2]+a[i],dp[i-1]))
dp.append(max(dp[n-3]+a[n-1],dp[n-4]+a[n-2]+a[n-1]))
print(dp[n-1])
