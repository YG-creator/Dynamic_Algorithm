n = int(input())
dp = [1] * 36
for i in range(2,n+1) :
    a = 0
    for j in range(i) :
        a += dp[j]*dp[i-1-j]
    dp[i] = a
print(dp[n])
